# 📊 ETF Weekly Report mit KI-Zusammenfassung & E-Mail-Versand

Dieses Projekt analysiert wöchentlich die Kursentwicklung eines ETFs (basierend auf ISIN), generiert eine kompakte KI-Zusammenfassung und verschickt das Ergebnis automatisch per E-Mail.  
**Kein API-Schlüssel nötig** – läuft vollständig automatisiert über GitHub Actions.

---

## 🔧 Features

- 📈 Wöchentliche Berechnung der Kursveränderung eines ETFs (z. B. über Xetra)
- 📬 Automatischer Versand des Berichts per E-Mail
- 🧠 KI-Zusammenfassung via Hugging Face (`google/flan-t5-small`) – **ohne Authentifizierung**
- 🕒 Wöchentlicher GitHub Actions Workflow (manuell und automatisch startbar)

---

## 📤 Beispiel-Report (E-Mail-Inhalt)

```text
ETF Report – Kalenderwoche 29

📌 ETF: SPDR MSCI All Country World Investable Market UCITS ETF (Acc)
📈 Wöchentliche Veränderung: -0.78 %

🧠 KI-Zusammenfassung:
Die Kursveränderung des ETFs könnte auf globale Marktverunsicherung, Veränderungen der Zinspolitik oder konjunkturelle Abschwächung zurückzuführen sein.
