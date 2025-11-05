# 🧠 NLP Brand Sentiment Analyzer

Analyze how people and the media feel about a brand using data from **Reddit** and **NewsAPI**.  
This project collects live data, cleans text using NLP, performs sentiment analysis, and visualizes insights.

---

## 🚀 Features
- Collects brand mentions from Reddit and News articles
- Cleans and preprocesses text (removes stopwords, URLs, punctuation)
- Performs **sentiment analysis** using VADER
- Shows visual insights (bar charts, word clouds)

---

## 🧰 How to Run

1. **Open the project folder**  
   Go to your folder: `NLP_Brand_Sentiment`

2. **Open your virtual environment (venv)**  
   In Git Bash:
   ```bash
   cd ~/Desktop/NLP_Brand_Sentiment
   source venv/Scripts/activate
   ```

3. **Run Jupyter Notebook**
   ```bash
   jupyter notebook
   ```
   Then open the notebook inside the `notebooks` folder.

4. **Run each cell step-by-step**
   You’ll see:
   - Data collected from Reddit + NewsAPI
   - Text cleaned
   - Sentiments detected
   - Charts and word clouds generated

---

## 📁 Project Structure
```
NLP_Brand_Sentiment/
├─ notebooks/
│  └─ NLP_Brand_Sentiment.ipynb
├─ src/
├─ snapshots/
├─ .env
└─ README.md
```

---

## ⚖️ Legal & Ethical Use
This project uses only **official free APIs**:
- **Reddit (PRAW)** — public data access  
- **NewsAPI** — free developer tier  

All data is used for **educational purposes** only.

---

## ▶️ How to Run the Streamlit App

You can explore the project interactively using **Streamlit**.

### 🧭 Steps

1. **Open a terminal** (Git Bash or CMD) inside your project folder:
   ```bash
   cd ~/Desktop/NLP_Brand_Sentiment
Activate your virtual environment:

bash

source venv/Scripts/activate   # For Git Bash
# or
venv\Scripts\activate          # For CMD or PowerShell
Move into the Streamlit folder:

bash

cd streamlit_app
Run the app:

bash

streamlit run app.py
After a few seconds, Streamlit will automatically open in your browser at
👉 http://localhost:8501

💡 Example
Enter any brand name (e.g., Flipkart, Apple, Tesla) to:

Fetch recent news & Reddit posts

Analyze their sentiment in real time

Visualize insights with charts and word clouds


---

## 👤 Author
**Krish @ IIT Roorkee**  
NLP & AI Enthusiast
