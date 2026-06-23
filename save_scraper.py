import requests
import json

PROMPT = """
Write a complete, professional Python web scraping script using BeautifulSoup and requests.
Include error handling for network issues and save the output to a CSV file.
Provide ONLY the raw executable Python code. Do not include any markdown code blocks (like ```python), explanations, or introduction. Start directly with the imports.
"""

url = "http://localhost:11434/api/generate"
payload = {
    "model": "llama3.1:8b",
    "prompt": PROMPT,
    "stream": False
}

print("🤖 الموديل بيصنع الكود وبيكتبه جوة الملف حالاً بدون نسخ...")
try:
    response = requests.post(url, json=payload)
    result = response.json().get('response', '')
    
    # تنظيف الكود لو الموديل استهبل وحط علامات الـ markdown
    if "```python" in result:
        result = result.split("```python")[1].split("```")[0]
    elif "```" in result:
        result = result.split("```")[1].split("```")[0]
        
    with open("scraper.py", "w", encoding="utf-8") as f:
        f.write(result.strip())
    print("\n✅ مبروك يا فنان! الملف اتصنع وبقى جاهز باسم: scraper.py")
except Exception as e:
    print(f"\n❌ حصلت مشكلة: {e}")
