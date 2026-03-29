import json
import requests

API_KEY = "AIzaSyBbl4QmrbgNv-U1k1RAfuoYOXuvT0z8JEo"

def handler(request):
    body = json.loads(request.body)
    user_input = body.get("mesaj", "")

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
