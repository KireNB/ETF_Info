import os
import requests

def get_ai_summary(etf_ticker, weekly_change):
    model_url = "https://api-inference.huggingface.co/models/google/flan-t5-small"

    prompt = (
        f"Der ETF mit dem Ticker {etf_ticker} hat sich in dieser Woche um {weekly_change:.2f}% verändert. "
        "Nenne mögliche Gründe für diese Kursveränderung in 2-3 kurzen Sätzen."
    )

    payload = {
        "inputs": f"Erkläre: {prompt}",
        "parameters": {
            "max_new_tokens": 100,
            "temperature": 0.7
        }
    }

    # >>> API-Key aus Umgebungsvariable laden und prüfen
    api_key = os.getenv("HUGGINGFACE_API_KEY")
    if not api_key:
        return "Fehler: HUGGINGFACE_API_KEY ist nicht gesetzt oder leer."

    headers = {
        "Authorization": f"Bearer {api_key}"
    }

    # >>> POST-Request an Hugging Face senden
    response = requests.post(model_url, json=payload, headers=headers)

    if response.status_code != 200:
        return f"Hugging Face API error: {response.status_code}, {response.text}"

    # >>> Ergebnis auswerten
    try:
        result = response.json()
        if isinstance(result, list) and "generated_text" in result[0]:
            return result[0]["generated_text"]
        elif isinstance(result, list):
            return result[0].get("generated_text", "Keine Zusammenfassung erhalten.")
        else:
            return f"Unerwartetes Antwortformat: {result}"
    except Exception as e:
        return f"Fehler bei der Verarbeitung der Antwort: {e}"

    return "Keine Zusammenfassung erhalten."


# Beispiel für Aufruf (optional, kann entfernt werden)
if __name__ == "__main__":
    print(get_ai_summary("SPY", 2.34))
