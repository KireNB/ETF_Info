import yfinance as yf
from datetime import datetime, timedelta
from gpt_summary import get_ai_summary
import smtplib
import os
from email.message import EmailMessage

# ISIN-Konfiguration
TARGET_ISIN = "IE00B3YLTY66"
ISIN_TO_TICKER = {
    "IE00B3YLTY66": {
        "ticker": "VWCE.DE",
        "name": "Vanguard FTSE All-World UCITS ETF",
    },
}

def get_last_week_change(ticker):
    today = datetime.today()
    last_week = today - timedelta(days=7)

    data = yf.download(
        ticker,
        start=last_week.strftime("%Y-%m-%d"),
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
    sender = os.getenv("EMAIL_USER")
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

    change = get_last_week_change(ticker)
    if change is None:
        print("❌ Nicht genügend Kursdaten verfügbar.")
        return

    summary = get_ai_summary(ticker, change)

    # Bericht zusammenbauen
    report = (
        f"📄 ETF: {name}\n"
        f"🔢 ISIN: {TARGET_ISIN}\n"
        f"📈 Ticker: {ticker}\n"
        f"📉 Veränderung letzte Woche: {change:.2f}%\n\n"
        f"🧠 KI-Zusammenfassung:\n{summary}"
    )

    print(report)

    # 📬 Mail senden
    send_email(f"📈 ETF-Wochenreport – {name}", report)

if __name__ == "__main__":
    main()
