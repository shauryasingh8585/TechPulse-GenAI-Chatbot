# 🤖 TechPulse AI – Generative AI Chatbot

A modern **Generative AI Chatbot** built using **Streamlit + LangChain + Groq**.

Users can ask technology-related questions and also click on predefined suggested questions to get instant answers.

---

## ✨ Features

- Clean and modern dark-themed chat interface
- Predefined suggested questions (clickable buttons)
- Free text input for any technology-related question
- Powered by **LangChain** + **Groq** (Llama 3.1)
- Works both locally and on Streamlit Community Cloud
- Secure API key handling (never exposed in code)

---

## 🛠️ Tech Stack

| Technology       | Purpose                          |
|------------------|----------------------------------|
| Streamlit        | Frontend & Web App Framework     |
| LangChain        | LLM Orchestration                |
| Groq             | Fast LLM Inference (Free tier)   |
| Llama 3.1 8B     | Language Model                   |
| python-dotenv    | Environment variable management  |

---

## 🚀 How to Run Locally

### 1. Clone the repository
```bash
git clone https://github.com/shauryasingh8585/TechPulse-GenAI-Chatbot.git
cd TechPulse-GenAI-Chatbot
```

### 2. Create virtual environment
```bash
python -m venv venv
venv\Scripts\activate          # Windows
# source venv/bin/activate     # Mac/Linux
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Add your Groq API Key
Create a file named `.env` in the project root:

```env
GROQ_API_KEY=your_actual_groq_api_key_here
```

**How to get a free Groq API Key:**
1. Go to → https://console.groq.com/keys
2. Sign up / Login
3. Create a new API Key
4. Copy and paste it in the `.env` file

### 5. Run the app
```bash
streamlit run app.py
```

The app will open at → http://localhost:8501

---

## ☁️ Deploy on Streamlit Community Cloud (Free)

1. Push your code to GitHub (already done)
2. Go to [https://share.streamlit.io](https://share.streamlit.io)
3. Sign in with your GitHub account
4. Click **New app**
5. Select the repository: `TechPulse-GenAI-Chatbot`
6. Main file path: `app.py`
7. Click **Advanced settings** → **Secrets**
8. Add this:
   ```toml
   GROQ_API_KEY = "your_actual_groq_api_key_here"
   ```
9. Click **Deploy**

Your public live link will be ready in 1–2 minutes!

---

## 📸 Screenshots

(Add screenshots of the chatbot here after running)

---

## 📁 Project Structure

```
TechPulse-GenAI-Chatbot/
├── app.py              # Main Streamlit application
├── requirements.txt    # Python dependencies
├── .gitignore
└── README.md
```

---

## 👨‍💻 Author

**Shaurya Singh**  
College Project – Generative AI Chatbot  
Built using Streamlit + LangChain + Groq

---

## 📄 License

This project is created for educational purposes.
```