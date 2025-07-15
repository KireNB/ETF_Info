import yfinance as yf
from datetime import datetime, timedelta
from gpt_summary import get_ai_summary

# 🆔 Hier trägst du deine Ziel-ISIN ein
TARGET_ISIN = "IE00B3YLTY66"

# 🗺️ Manuelles Mapping von ISIN → Ticker (kann erweitert werden)
ISIN_TO_TICKER = {
    "IE00B3YLTY66": {
        "ticker": "VWCE.DE",  # Vanguard FTSE All-World UCITS ETF (EUR)
        "name": "Vanguard FTSE All-World UCITS ETF",
    },
    "US78462F1030": {
        "ticker": "SPY",
        "name": "SPDR S&P 500 ETF Trust",
    },
    # Weitere ISINs hier einfügen
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

def main():
    etf_info = ISIN_TO_TICKER.get(TARGET_ISIN)

    if not etf_info:
        print(f"❌ ISIN {TARGET_ISIN} ist nicht in der Mapping-Tabelle vorhanden.")
        return

    ticker = etf_info["ticker"]
    name = etf_info["name"]

    change = get_last_week_change(ticker)
    if change is None:
        print("❌ Nicht genügend Kursdaten verfügbar.")
        return

    summary = get_ai_summary(ticker, change)

    print(f"📄 ETF: {name}")
    print(f"🔢 ISIN: {TARGET_ISIN}")
    print(f"📈 Ticker: {ticker}")
    print(f"📉 Veränderung letzte Woche: {change:.2f}%")
    print("🧠 KI-Zusammenfassung:")
    print(summary)

if __name__ == "__main__":
    main()
