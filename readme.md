# 📊 ETF Weekly Report Bot

Automatischer ETF-Report direkt in deine Mailbox – inklusive KI-Zusammenfassung über die Kursentwicklung deines ETFs.  
Dieses Projekt nutzt **[Yahoo Finance](https://finance.yahoo.com)**, **Hugging Face Transformers** und **GitHub Actions**, um dir jede Woche (oder auf Knopfdruck) ein kurzes Marktupdate zu liefern.

---

## 🧠 Was macht das Tool?

✔️ Wöchentliche Kursveränderung deines ETFs berechnen  
✔️ Automatische Interpretation durch eine KI (z. B. Hugging Face Modell)  
✔️ Ausgabe im Terminal oder per Mail  
✔️ Kompatibel mit ISIN-Eingabe statt Ticker  
✔️ Vollständig automatisiert via GitHub Actions oder manuell ausführbar

---

## ⚙️ Projektstruktur

```bash
ETF_Info/
├── main.py              # Hauptlogik: Kursdaten laden, KI-Zusammenfassung
├── gpt_summary.py       # KI-Logik über Hugging Face oder OpenAI
├── .github/workflows/
│   └── etf_report.yml   # GitHub Actions Workflow (automatisch & manuell)
├── requirements.txt     # Abhängigkeiten
└── README.md            # Diese Datei
