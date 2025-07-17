# 📊 ETF Monatsreport mit KI-Analyse & E-Mail-Versand

Dieses Projekt analysiert **monatlich** die Kursentwicklung eines ETFs (basierend auf ISIN), generiert eine **faktenbasierte GPT-Zusammenfassung mit drei Hauptfaktoren** und versendet das Ergebnis automatisch per E-Mail.  
Die Ausführung erfolgt automatisiert über **GitHub Actions**.

---

## 🔧 Features

- 📈 **Monatliche** Kursveränderung eines globalen ETFs (z. B. über Xetra)
- 🧠 KI-Zusammenfassung via **OpenRouter API** (z. B. DeepSeek, Mixtral etc.)
- 📬 Automatischer Versand des Reports per E-Mail (SMTP)
- 🔁 GitHub Actions Workflow: Monatlich & manuell startbar
- 🔒 Verwendung von Secrets für API-Keys und Zugangsdaten

---

## 🗓 Zeitplan (GitHub Actions)

- ⏰ **Automatisch jeden Monat am 1. Tag um 08:00 UTC**
- 🖱 Zusätzlich manuell per Button ausführbar (`workflow_dispatch`)

---

## 📤 Beispiel-Report (E-Mail-Inhalt)

```text
📄 ETF: SPDR MSCI All Country World Investable Market UCITS ETF (Acc)
🔢 ISIN: IE00B3YLTY66
📈 Ticker: SPYI.DE
📆 Veränderung im laufenden Monat: -1.72%

1. Die US-Inflationsrate für Juni lag über den Erwartungen, was Zinssorgen verstärkte.
2. Die chinesischen Exportzahlen fielen schwach aus und belasteten die globale Konjunkturstimmung.
3. Die Spannungen im Nahen Osten führten zu verstärkter Risikoaversion bei Investoren.
