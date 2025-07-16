import os
import requests
import logging

# Logging für Fehlersuche
logging.basicConfig(
    filename="llm_api.log",
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def get_ai_summary(etf_name, weekly_change):
    prompt = (
        f"Der ETF '{etf_name}' hat in der vergangenen Woche eine Kursveränderung von {weekly_change:.2f}% gezeigt. "
        "Fasse in drei klaren und präzisen Sätzen auf Deutsch zusammen, welche globalen wirtschaftlichen, politischen oder "
        "marktbezogenen Entwicklungen in diesem Zeitraum wahrscheinlich zu dieser Kursbewegung geführt haben. "
        "Formuliere professionell, faktenbasiert und ohne vage Spekulationen."
    )

    api_key = os.getenv("OPENROUTER_API_KEY")
    if not api_key:
        return "Fehler: OPENROUTER_API_KEY ist nicht gesetzt."

    headers = {
        "Authorization": f"Bearer {api_key}",
        "HTTP-Referer": "https://deinprojekt.de",
        "X-Title": "ETF-Report",
        "Content-Type": "application/json"
    }

    payload = {
        "model": "tngtech/deepseek-r1t-chimera:free",
        "messages": [
            {"role": "system", "content": "Fasse ETF-Entwicklungen sachlich, professionell und auf Deutsch zusammen."},
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
