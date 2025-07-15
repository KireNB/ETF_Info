import os
import requests

def get_ai_summary(etf_ticker, weekly_change):
    model_url = "https://api-inference.huggingface.co/models/mistralai/Mistral-7B-Instruct-v0.1"

    prompt = (
        f"Der ETF mit dem Ticker {etf_ticker} hat sich in dieser Woche um {weekly_change:.2f}% verändert. "
        "Welche möglichen Gründe gibt es dafür? Antworte in 2-3 kurzen Sätzen."
    )

    payload = {
        "inputs": prompt,
        "parameters": {
            "max_new_tokens": 150,
            "temperature": 0.7
        }
    }

    # API-Key laden
    api_key = os.getenv("HUGGINGFACE_API_KEY")
    if not api_key:
        return "Fehler: HUGGINGFACE_API_KEY ist nicht gesetzt oder leer."

    headers = {
        "Authorization": f"Bearer {api_key}"
    }

    response = requests.post(model_url, json=payload, headers=headers)

    if response.status_code != 200:
        return f"Hugging Face API error: {response.status_code}, {response.text}"

    try:
        result = response.json()

        # Je nach API-Antwortformat
        if isinstance(result, list) and "generated_text" in result[0]:
            return result[0]["generated_text"]
        elif isinstance(result, dict) and "generated_text" in result:
            return result["generated_text"]
        else:
            return f"Unerwartetes Antwortformat: {result}"
    except Exception as e:
        return f"Fehler bei der Verarbeitung der Antwort: {e}"

    return "Keine Zusammenfassung erhalten."


# Optionaler Testaufruf
if __name__ == "__main__":
    print(get_ai_summary("SPY", 2.34))
