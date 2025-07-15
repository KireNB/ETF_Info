import os
import requests

HUGGINGFACE_API_KEY = os.getenv("HUGGINGFACE_API_KEY")
API_URL = "https://api-inference.huggingface.co/models/mistralai/Mistral-7B-Instruct-v0.1"
HEADERS = {"Authorization": f"Bearer {HUGGINGFACE_API_KEY}"}

def get_ai_summary(etf_ticker, weekly_change):
    prompt = (
        f"Der ETF {etf_ticker} hat sich in dieser Woche um {weekly_change:.2f}% verändert.\n"
        f"Erkläre in 2–3 Sätzen, was mögliche makroökonomische oder marktpsychologische Gründe dafür sein könnten."
    )

    response = requests.post(API_URL, headers=HEADERS, json={"inputs": prompt})

    if response.status_code == 200:
        result = response.json()
        if isinstance(result, list) and "generated_text" in result[0]:
            return result[0]["generated_text"]
        elif isinstance(result, dict) and "generated_text" in result:
            return result["generated_text"]
        else:
            return "Keine sinnvolle Antwort vom KI-Modell erhalten."
    else:
        return f"Fehler bei Hugging Face API: {response.status_code}, {response.text}"
