import os
import requests
import logging

# Logging für Fehlersuche
logging.basicConfig(
    filename="llm_api.log",
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def get_ai_summary(etf_name, monthly_change):
    prompt = (
        f"Der ETF '{etf_name}' hat im vergangenen Monat eine Kursveränderung von {monthly_change:.2f}% gezeigt. "
        "Nenne die drei wahrscheinlichsten Ursachen dafür – nummeriert, knapp und faktenbasiert. "
        "Schreibe auf Deutsch. Keine Einleitung, kein Fazit. Nur die drei Gründe."
    )

    api_key = os.getenv("OPENROUTER_API_KEY")
    if not api_key:
        return "Fehler: OPENROUTER_API_KEY ist nicht gesetzt."

    headers = {
        "Authorization": f"Bearer {api_key}",
        "HTTP-Referer": "https://deinprojekt.de",
        "X-Title": "ETF-Monatsanalyse",
        "Content-Type": "application/json"
    }

    payload = {
        "model": "tngtech/deepseek-r1t-chimera:free",
        "messages": [
            {
                "role": "system",
                "content": (
                    "Du bist ein erfahrener Finanzanalyst und gibst monatlich drei präzise Gründe für die Kursentwicklung eines ETFs. "
                    "Deine Antwort besteht ausschließlich aus den drei nummerierten Gründen – keine Einleitung, kein Fazit, keine Wiederholung der Frage."
                )
            },
            {"role": "user", "content": prompt}
        ],
        "temperature": 0.5,
        "max_tokens": 1000
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
