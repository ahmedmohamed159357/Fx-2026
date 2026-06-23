import requests
import json

PROMPT = """
اكتب لي سكريبت بايثون احترافي يسحب بيانات من صفحة ويب (Web Scraping)، 
وينظف الداتا دي ويحفظها في ملف CSV، مع معالجة الأخطاء (Error Handling) لو الموقع هنج.
"""

url = "http://localhost:11434/api/generate"
payload = {
    "model": "llama3.1:8b",
    "prompt": PROMPT,
    "stream": True
}

print("🤖 الموديل بيصيغ الكود دلوقتي يا هندسة...\n")
try:
    response = requests.post(url, json=payload, stream=True)
    for line in response.iter_lines():
        if line:
            chunk = json.loads(line.decode('utf-8'))
            print(chunk.get('response', ''), end='', flush=True)
except Exception as e:
    print(f"\n❌ حصلت مشكلة: {e}")
