import os
import requests
import logging

# Logging für Fehlersuche
logging.basicConfig(
    filename="llm_api.log",
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def get_ai_summary(etf_ticker, weekly_change):
    prompt = (
        f"Der ETF mit dem Ticker {etf_ticker} hat sich in dieser Woche um {weekly_change:.2f}% verändert. "
        "Nenne mögliche Gründe für diese Kursveränderung in 2-3 kurzen Sätzen."
    )

    api_key = os.getenv("OPENROUTER_API_KEY")
    if not api_key:
        return "Fehler: OPENROUTER_API_KEY ist nicht gesetzt."

    headers = {
        "Authorization": f"Bearer {api_key}",
        "HTTP-Referer": "https://deine-seite.de",  # optional, aber empfohlen laut OpenRouter
        "X-Title": "ETF-Report",                  # optional: Projekttitel
        "Content-Type": "application/json"
    }

    payload = {
        "model": "tngtech/deepseek-r1t-chimera:free",  # ✅ Kostenlose Variante
        "messages": [
            {"role": "system", "content": "Fasse ETF-Entwicklungen kurz und verständlich zusammen."},
            {"role": "user", "content": prompt}
        ],
        "temperature": 0.7,
        "max_tokens": 150
    }

    try:
        response = requests.post("https://openrouter.ai/api/v1/chat/completions", headers=headers, json=payload)
        logging.debug("OpenRouter-Response: %s", response.text)

        if response.status_code != 200:
            return f"OpenRouter API error: {response.status_code}, {response.text}"

        result = response.json()
        return result["choices"][0]["message"]["content"].strip()

    except Exception as e:
        logging.error("Fehler bei OpenRouter-Anfrage: %s", e)
        return f"Fehler bei der Anfrage: {e}"


# import os
# import requests

# def get_ai_summary(etf_ticker, weekly_change):
#     model_url = "https://api-inference.huggingface.co/models/google/flan-t5-base"

#     prompt = (
#         f"Der ETF mit dem Ticker {etf_ticker} hat sich in dieser Woche um {weekly_change:.2f}% verändert. "
#         "Nenne mögliche Gründe für diese Kursveränderung in 2-3 kurzen Sätzen."
#     )

#     payload = {
#         "inputs": f"Erkläre: {prompt}",
#         "parameters": {
#             "max_new_tokens": 100,
#             "temperature": 0.7
#         }
#     }

#     api_key = os.getenv("HUGGINGFACE_API_KEY")
#     if not api_key:
#         return "Fehler: HUGGINGFACE_API_KEY ist nicht gesetzt."

#     headers = {
#         "Authorization": f"Bearer {api_key}"
#     }

#     response = requests.post(model_url, headers=headers, json=payload)

#     if response.status_code != 200:
#         return f"Hugging Face API error: {response.status_code}, {response.text}"

#     try:
#         result = response.json()
#         if isinstance(result, list) and "generated_text" in result[0]:
#             return result[0]["generated_text"]
#         elif isinstance(result, list):
#             return result[0].get("generated_text", "Keine Zusammenfassung erhalten.")
#         else:
#             return f"Unerwartetes Antwortformat: {result}"
#     except Exception as e:
#         return f"Fehler bei der Verarbeitung der Antwort: {e}"

#     return "Keine Zusammenfassung erhalten."
