import os
from report_generator import get_weekly_performance
from email_sender import send_email
from gpt_summary import get_ai_summary

ETF_TICKER = "VWCE.DE"

def main():
    change, start_price, end_price = get_weekly_performance(ETF_TICKER)
    if change is None:
        return

    summary = get_ai_summary(ETF_TICKER, change)

    report = (
        f"ETF-Report für {ETF_TICKER}\n\n"
        f"Start: {start_price:.2f} €\nEnde: {end_price:.2f} €\n"
        f"Veränderung: {change:.2f}%\n\n"
        f"GPT-Zusammenfassung:\n{summary}"
    )

    send_email(f"ETF Report: {ETF_TICKER}", report)

if __name__ == "__main__":
    main()
