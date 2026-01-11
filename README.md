# 🔐 Link Safety Checker

A free, open-source web application that analyzes URLs and flags potential security risks using **heuristic-based analysis**.

The tool is designed to help users quickly identify **suspicious, obfuscated, or potentially malicious links** before clicking them.

> ⚠️ This project focuses on explainable heuristics, not black-box detection.

---

## 🌐 Live Demo
👉 (https://link-safety-checker-xwylgkquvgawgbd4vvqjbe.streamlit.app/)

---

## 🚀 Features

- ✅ HTTPS validation
- 🧠 Suspicious keyword detection
- 🌍 IP-based URL detection
- ⏱️ Domain age analysis (WHOIS)
- 🔁 Redirect chain detection
- 📏 URL path length analysis
- 🎲 Entropy-based obfuscation detection
- 🚩 High-risk TLD detection
- 📊 Risk scoring with clear explanations
- 🎨 Clean Streamlit web interface

---

## 🧠 How It Works

The Link Safety Checker uses **heuristic analysis** to evaluate URLs.  
Each detected risk factor contributes to a cumulative **risk score**, which is then mapped to a verdict:

| Score Range | Verdict |
|-----------|--------|
| 0 – 30 | ✅ Safe |
| 31 – 60 | ⚠️ Suspicious |
| 61+ | ❌ Dangerous |

### Examples of Heuristics Used
- Extremely long or deeply nested URL paths
- High randomness (entropy) in URL structure
- Use of high-risk top-level domains (e.g. `.shop`, `.xyz`)
- Multiple redirects
- Very new domains
- Lack of HTTPS

Each result includes **human-readable reasons**, making the decision transparent.

---

## 🧪 Why Heuristics?

Modern malicious links often:
- Use valid HTTPS
- Avoid obvious phishing keywords
- Hide behind clean-looking domains

Heuristic analysis helps detect **behavioral and structural red flags** that traditional checks may miss.

This project intentionally highlights:
- ✔️ Strengths of heuristic detection  
- ⚠️ Its limitations  

This mirrors how real-world security tools operate.

---

## 🛠️ Tech Stack

- **Python**
- **Streamlit**
- `requests`
- `validators`
- `python-whois`

All components are **100% free** and open source.

---

## ▶️ Run Locally

### 1️⃣ Clone the repository
```bash
git clone https://github.com/your-username/link-safety-checker.git
cd link-safety-checker
