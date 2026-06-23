import os
from bs4 import BeautifulSoup
import requests
import csv
import time

def scrape_data(url):
    # حطينا هيدر (User-Agent) عشان الموقع ما يفتكرناش بوت ويقفل الـ Request
    headers = {
        'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36'
    }
    try:git add .
    git commit -m "Unzipped project files"
    git push origin main
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            
            title = soup.find('title').text.strip() if soup.find('title') else 'No Title'
            
            # هنسحب كل النصوص والفقرات اللي في الصفحة عشان تلم الداتا اللي شوفتها في الصور
            paragraphs = [p.text.strip() for p in soup.find_all('p') if p.text.strip()]
            paragraph_text = " | ".join(paragraphs[:5]) # هناخد أول 5 فقرات كمثال
            
            return {
                'Title': title,
                'Paragraph': paragraph_text
            }
        else:
            print(f'Failed to retrieve data. Status code: {response.status_code}')
            time.sleep(2)
    except requests.exceptions.RequestException as e:
        print(f'Network error occurred: {e}')

def save_to_csv(data, filename):
    # تصليح ذكي: التأكد إن الملف موجود وله حجم قبل ما نقيسه عشان ما يكرشش
    file_exists = os.path.exists(filename) and os.path.getsize(filename) > 0
    
    with open(filename, 'a', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['Title', 'Paragraph']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        
        if not file_exists:
            writer.writeheader()
        
        writer.writerow(data)
        print(f'✅ تم إضافة البيانات بنجاح في ملف: {filename}')

def main():
    # حطيت لك رابط الموقع اللي كان في السكرين شوت بتاعك عشان نجرب عليه علطول!
    url = 'https://d6bqezc.ok.kimi.link'
    print(f'🔄 جاري سحب البيانات من: {url} ...')
    data = scrape_data(url)
    
    if data is not None:
        filename = 'scraped_data.csv'
        save_to_csv(data, filename)

if __name__ == '__main__':
    main()
