
import os
import requests

def get_ai_summary(etf_ticker, weekly_change):
    hf_token = os.getenv("HUGGINGFACE_API_KEY")
    headers = {"Authorization": f"Bearer {hf_token}"}

    model_url = "https://api-inference.huggingface.co/models/bigscience/bloomz-560m"

    prompt = (
        f"Der ETF mit dem Ticker {etf_ticker} hat sich in dieser Woche um {weekly_change:.2f}% verändert. "
        "Nenne in 2-3 kurzen Sätzen mögliche Gründe für die Kursentwicklung."
    )

    payload = {
        "inputs": prompt,
        "parameters": {
            "max_new_tokens": 100,
            "do_sample": True,
            "temperature": 0.7
        }
    }

    response = requests.post(model_url, headers=headers, json=payload)

    if response.status_code != 200:
        return f"Fehler bei Hugging Face API: {response.status_code}, {response.text}"

    result = response.json()
    
    # Je nach Modellformat: manchmal ist es direkt ein String, manchmal ein Dict
    if isinstance(result, list) and "generated_text" in result[0]:
        return result[0]["generated_text"]
    elif isinstance(result, dict) and "generated_text" in result:
        return result["generated_text"]
    else:
        return "Keine Zusammenfassung erhalten."

