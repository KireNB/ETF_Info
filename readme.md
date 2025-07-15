# 📊 ETF Weekly Report mit KI-Zusammenfassung & E-Mail-Versand

Dieses Projekt analysiert wöchentlich die Kursentwicklung eines ausgewählten ETFs anhand seiner **ISIN** und versendet einen kompakten Report per E-Mail. Zusätzlich wird eine KI-basierte Zusammenfassung der möglichen Kursbewegungen generiert – ganz ohne OpenAI oder API-Kosten!

---

## 🔧 Features

- 📈 Berechnung der wöchentlichen Kursänderung eines ETFs
- 📬 Automatischer Versand eines E-Mail-Reports
- 🧠 KI-Zusammenfassung möglicher Kursursachen via Hugging Face (ohne API-Key)
- ⏱ Automatische Ausführung via GitHub Actions (wöchentlich & manuell triggerbar)

---

## 🔎 Beispielausgabe

```text
ETF Report – Kalenderwoche 28

📌 ETF: SPDR MSCI All Country World Investable Market UCITS ETF (Acc)
📈 Wöchentliche Veränderung: +1.34%

🧠 KI-Zusammenfassung:
Die Kursentwicklung des ETFs könnte mit globalen Marktbewegungen, Zentralbankentscheidungen oder makroökonomischen Trends in Zusammenhang stehen.
