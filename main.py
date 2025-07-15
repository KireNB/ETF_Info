import yfinance as yf
from datetime import datetime, timedelta
from gpt_summary import get_ai_summary

ETF_TICKER = "SPY"

def get_last_week_change(ticker):
    today = datetime.today()
    last_week = today - timedelta(days=7)
    
    data = yf.download(ticker, start=last_week.strftime("%Y-%m-%d"), end=today.strftime("%Y-%m-%d"))
    if len(data) < 2:
        return None

    start_price = data["Close"].iloc[0]
    end_price = data["Close"].iloc[-1]
    change_percent = ((end_price - start_price) / start_price) * 100
    return round(change_percent, 2)

def main():
    change = get_last_week_change(ETF_TICKER)
    if change is None:
        print("Nicht genügend Kursdaten verfügbar.")
        return

    summary = get_ai_summary(ETF_TICKER, change)
    print(f"📈 {ETF_TICKER} Veränderung: {change:.2f}%")
    print("🧠 KI-Zusammenfassung:")
    print(summary)

if __name__ == "__main__":
    main()


# import os
# from report_generator import get_weekly_performance
# from email_sender import send_email
# from gpt_summary import get_ai_summary

# ETF_TICKER = "VWCE.DE"

# def main():
#     change, start_price, end_price = get_weekly_performance(ETF_TICKER)
#     if change is None:
#         return

#     summary = get_ai_summary(ETF_TICKER, change)

#     report = (
#         f"ETF-Report für {ETF_TICKER}\n\n"
#         f"Start: {start_price:.2f} €\nEnde: {end_price:.2f} €\n"
#         f"Veränderung: {change:.2f}%\n\n"
#         f"GPT-Zusammenfassung:\n{summary}"
#     )

#     send_email(f"ETF Report: {ETF_TICKER}", report)

# if __name__ == "__main__":
#     main()
