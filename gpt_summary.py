import requests

def get_ai_summary(etf_ticker, weekly_change):
    model_url = "https://api-inference.huggingface.co/models/mrm8488/t5-base-finetuned-question-generation-ap"

    prompt = (
        f"Der ETF mit dem Ticker {etf_ticker} hat sich in dieser Woche um {weekly_change:.2f}% verändert. "
        "Was könnten mögliche Gründe für diese Veränderung sein?"
    )

    payload = {
        "inputs": prompt,
        "parameters": {
            "max_new_tokens": 100,
            "do_sample": True,
            "temperature": 0.7
        }
    }

    response = requests.post(model_url, json=payload)

    if response.status_code != 200:
        return f"Hugging Face API error: {response.status_code}, {response.text}"

    result = response.json()

    if isinstance(result, list) and "generated_text" in result[0]:
        return result[0]["generated_text"]
    elif isinstance(result, dict) and "generated_text" in result:
        return result["generated_text"]
    else:
        return "Keine Zusammenfassung erhalten."
