import json
import requests

API_KEY = "BURAYA_API_KEY_YAPIŞTIR"

def handler(request):
    user_input = "Merhaba"

    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent?key={API_KEY}"

    headers = {
        "Content-Type": "application/json"
    }

    data = {
        "contents": [
            {
                "parts": [
                    {"text": user_input}
                ]
            }
        ]
    }

    res = requests.post(url, headers=headers, json=data)
    cevap = res.json()

    try:
        text = cevap["candidates"][0]["content"]["parts"][0]["text"]
    except:
        text = "Hata oluştu"

    return {
        "statusCode": 200,
        "body": json.dumps({"response": text}),
        "headers": {
            "Content-Type": "application/json"
        }
    }
