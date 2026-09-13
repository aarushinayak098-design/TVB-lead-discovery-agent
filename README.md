# 🔎 TVB Lead Discovery Agent

An automated lead discovery and qualification agent designed for **The Venture Build (TVB)** profile. This application discovers and filters potential B2B technology leads against TVB's core investment and acquisition qualification criteria.

---

## 🚀 Live Demo & Repository Links

- 🔗 **Live Streamlit App:** [https://tvb-lead-discovery-agent.streamlit.app](https://tvb-lead-discovery-agent.streamlit.app)
- 🐙 **GitHub Repository:** [https://github.com/aarushinayak098-design/TVB-lead-discovery-agent](https://github.com/aarushinayak098-design/TVB-lead-discovery-agent)

---

## ✨ Features

- 🔎 **Automated Discovery Engine:** Discovers target technology companies matching customizable search thresholds.
- 🎯 **Rule-Based Qualification:** Transparently checks companies against 5 strict qualification rules.
- 📊 **Executive Dashboard:** Displays key performance metrics including Total Discovered, Qualified Leads, Founder/CEO Identified, and Public Email Availability.
- 📋 **Detailed Data Views:** Provides side-by-side comparative views for both qualified leads and all candidate companies.
- 🧠 **Explainable Logic:** Clear qualification reason tags generated for every evaluated record.
- 📥 **One-Click CSV Export:** Instantly download filtered lead data into CSV format for CRM integration.
- 🆓 **Zero API Dependencies:** Runs out of the box with zero external API key requirements.

---

## 🎯 Qualification Criteria

A company is categorized as **Qualified** only when all 5 conditions are met:

1. 💰 **Funding / Revenue:** Must be within **$1M – $5M**.
2. 💻 **Business Sector:** Must be a **Technology platform / SaaS / AI / Software** company.
3. 🇺🇸 **US Presence:** Minimal or no existing US presence.
4. 👤 **Key Contact:** Founder, Co-Founder, or CEO information identified.
5. 📧 **Direct Contact:** Valid public business email available.

---

## 🛠️ Tech Stack

- **Language:** Python 3.9+
- **Frontend / Framework:** [Streamlit](https://streamlit.io/)
- **Data Processing:** [Pandas](https://pandas.pydata.org/)
- **HTML Parsing & Web Tools:** BeautifulSoup4, Requests, lxml

---

## 📁 Project Structure

```
TVB project/
├── app.py              # Main Streamlit web application & user interface
├── agent.py            # Lead discovery engine & qualification logic
├── requirements.txt    # Python dependencies for deployment
├── .gitignore          # Git exclusion config
└── README.md           # Project documentation
```

---

## 💻 Local Quickstart Guide

Follow these steps to run the application locally on your machine:

### 1. Clone the Repository
```bash
git clone https://github.com/aarushinayak098-design/TVB-lead-discovery-agent.git
cd TVB-lead-discovery-agent
```

### 2. Create and Activate Virtual Environment
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS / Linux
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Run the Streamlit App
```bash
streamlit run app.py
```

Open your browser and navigate to `http://localhost:8501`.

---

## ☁️ How to Deploy on Streamlit Community Cloud (Free)

Deploying this app live for free takes less than 2 minutes:

1. Push this repository to your GitHub account: `https://github.com/aarushinayak098-design/TVB-lead-discovery-agent.git`
2. Go to [share.streamlit.io](https://share.streamlit.io/) and log in with your GitHub account.
3. Click **"New app"**.
4. Select repository: `aarushinayak098-design/TVB-lead-discovery-agent`
5. Set **Main file path** to: `app.py`
6. Click **"Deploy!"** 🚀

Once deployed, copy your live link (`https://<your-app-name>.streamlit.app`) for form submission!

---

## 🛡️ Synthetic Data Disclaimer

*Note: For project demonstration and evaluation purposes, synthetic company records are utilized to showcase the complete qualification pipeline and UI without relying on paid private APIs or exposing sensitive private data.*
