import yfinance as yf
from datetime import datetime
from gpt_summary import get_ai_summary
import smtplib
import os
from email.message import EmailMessage

# ISIN-Konfiguration
TARGET_ISIN = "IE00B3YLTY66"
ISIN_TO_TICKER = {
    "IE00B3YLTY66": {
        "ticker": "SPYI.DE",  # Ticker laut Yahoo Finance
        "name": "SPDR MSCI All Country World Investable Market UCITS ETF (Acc)",
    },
}

def get_last_month_change(ticker):
    today = datetime.today()
    month_start = today.replace(day=1)

    data = yf.download(
        ticker,
        start=month_start.strftime("%Y-%m-%d"),
        end=today.strftime("%Y-%m-%d"),
        auto_adjust=True
    )

    if len(data) < 2:
        return None

    start_price = float(data["Close"].iloc[0])
    end_price = float(data["Close"].iloc[-1])
    change_percent = ((end_price - start_price) / start_price) * 100
    return round(change_percent, 2)

def send_email(subject, body):
    sender = os.getenv("EMAIL_SENDER")
    password = os.getenv("EMAIL_PASSWORD")
    receiver = os.getenv("EMAIL_RECEIVER")

    msg = EmailMessage()
    msg["From"] = sender
    msg["To"] = receiver
    msg["Subject"] = subject
    msg.set_content(body)

    try:
        with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
            smtp.starttls()
            smtp.login(sender, password)
            smtp.send_message(msg)
        print("📬 E-Mail erfolgreich versendet.")
    except Exception as e:
        print(f"❌ Fehler beim E-Mail-Versand: {e}")

def main():
    etf_info = ISIN_TO_TICKER.get(TARGET_ISIN)
    if not etf_info:
        print(f"❌ ISIN {TARGET_ISIN} ist nicht bekannt.")
        return

    ticker = etf_info["ticker"]
    name = etf_info["name"]

    change = get_last_month_change(ticker)
    if change is None:
        print("❌ Nicht genügend Kursdaten verfügbar.")
        return

    summary = get_ai_summary(name, change)

    # Monatsbericht ohne Einleitung
    report = (
        f"📄 ETF: {name}\n"
        f"🔢 ISIN: {TARGET_ISIN}\n"
        f"📈 Ticker: {ticker}\n"
        f"📆 Veränderung im laufenden Monat: {change:.2f}%\n\n"
        f"{summary}"  # Nur die 3 Gründe
    )

    print(report)

    # E-Mail versenden
    send_email(f"📊 ETF-Monatsreport – {name}", report)

if __name__ == "__main__":
    main()
