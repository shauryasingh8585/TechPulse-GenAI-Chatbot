# TechPulse AI – GenAI Chatbot

A **Generative AI Chatbot** built with **Streamlit + LangChain + Groq**.

Users can ask **any technology-related question** either by typing freely or by clicking **predefined suggested questions**.

The chatbot uses LangChain + Groq. It has a built-in knowledge base for common topics and can also answer general technology, programming, and AI questions.

---

## Features

- Beautiful Streamlit chat interface
- **Predefined Questions** sidebar (click to ask instantly)
- Can answer **any technology-related question** (not limited to predefined ones)
- Powered by **LangChain** + **Groq** (free & very fast)
- Uses Llama 3.3 70B model
- Conversation memory (context-aware replies)
- Clear Chat button
- Fully educational project for college submission

---

## Tech Stack

| Component       | Technology              |
|-----------------|-------------------------|
| Framework       | Streamlit               |
| Orchestration   | LangChain               |
| LLM Provider    | Groq (Free tier)        |
| Model           | Llama 3.3 70B Versatile |
| Environment     | python-dotenv           |

---

## Project Structure

```
techpulse-genai-chatbot/
├── app.py                 # Main Streamlit application
├── requirements.txt       # Python dependencies
├── .env.example           # Template for API key
├── .gitignore
└── README.md
```

---

## How to Run

### 1. Clone / Download the project

### 2. Create virtual environment (recommended)

```bash
python -m venv venv

# Windows
venv\Scripts\activate

# Mac / Linux
source venv/bin/activate
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

The app will open at → `http://localhost:8501`

---

## Predefined Topics

The chatbot is designed to answer questions about:

- Artificial Intelligence (AI)
- Machine Learning & Deep Learning
- Generative AI & Large Language Models (LLMs)
- MERN Stack
- React.js & Node.js
- Cloud Computing
- Cybersecurity
- Blockchain
- Prompt Engineering

---

## Why Groq?

- Completely **free** tier available
- Extremely fast inference
- Excellent support for Llama models
- Easy integration with LangChain (`langchain-groq`)

---

## Important Notes

- Never upload your real `.env` file to GitHub
- Always use `.env.example` as a template
- This project is for educational / college submission purposes

---

## Author

**SHAURYA SINGH**  
College Assignment – Generative AI Project  
Built with Streamlit + LangChain + Groq

---

## License

Educational use only.
