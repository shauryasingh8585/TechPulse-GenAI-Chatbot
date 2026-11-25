import streamlit as st
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
import os

# Load environment variables (for local development)
load_dotenv()

# Page configuration
st.set_page_config(
    page_title="TechPulse AI - GenAI Chatbot",
    page_icon="🤖",
    layout="wide"
)

# Custom CSS for better look
st.markdown("""
<style>
    .stApp {
        background-color: #0e1117;
    }
    .main-header {
        text-align: center;
        color: #00d4ff;
        font-size: 2.5rem;
        font-weight: bold;
        margin-bottom: 0.5rem;
    }
    .sub-header {
        text-align: center;
        color: #aaaaaa;
        margin-bottom: 2rem;
    }
    .stButton > button {
        width: 100%;
        border-radius: 8px;
        background-color: #1e293b;
        border: 1px solid #334155;
        color: white;
    }
    .stButton > button:hover {
        background-color: #00d4ff;
        color: black;
        border-color: #00d4ff;
    }
</style>
""", unsafe_allow_html=True)

# Header
st.markdown('<div class="main-header">🤖 TechPulse AI</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-header">Your Intelligent Technology Assistant | Powered by LangChain + Groq</div>', unsafe_allow_html=True)

# Predefined questions
PREDEFINED_QUESTIONS = [
    "What is the MERN Stack?",
    "Explain Artificial Intelligence in simple words",
    "What is Machine Learning?",
    "What is RAG (Retrieval Augmented Generation)?",
    "Difference between Frontend and Backend",
    "What is an API?",
    "Explain LangChain",
    "What is Streamlit?",
    "What is Generative AI?",
    "How does ChatGPT work?"
]

# Get API Key (works both locally and on Streamlit Cloud)
def get_api_key():
    # First try Streamlit secrets (for deployment)
    try:
        return st.secrets["GROQ_API_KEY"]
    except:
        # Fallback to environment variable (for local)
        return os.getenv("GROQ_API_KEY")

api_key = get_api_key()

if not api_key:
    st.error("⚠️ GROQ_API_KEY not found!")
    st.info("""
    **For Local Run:** Create a `.env` file and add:
    ```
    GROQ_API_KEY=your_key_here
    ```
    
    **For Streamlit Cloud:** Go to App Settings → Secrets and add:
    ```
    GROQ_API_KEY = "your_key_here"
    ```
    """)
    st.stop()

# Initialize the LLM
@st.cache_resource
def get_llm():
    return ChatGroq(
        model="llama-3.1-8b-instant",  # Free & fast model on Groq
        temperature=0.3,
        groq_api_key=api_key
    )

llm = get_llm()

# System prompt
system_prompt = """You are TechPulse AI, a helpful and knowledgeable technology assistant.

You specialize in:
- Programming (Python, JavaScript, React, Node.js, MERN stack)
- Artificial Intelligence, Machine Learning, Generative AI
- Web Development, APIs, Databases
- Tools like Streamlit, LangChain, Docker, etc.

Guidelines:
1. Give clear, accurate, and concise answers.
2. Use simple language when possible.
3. Structure answers with bullet points or short paragraphs for readability.
4. If the question is completely unrelated to technology (e.g. sports, politics, personal advice), politely say: "I specialize in technology topics. Please ask me something related to programming, AI, or web development."
5. Be friendly and encouraging.
"""

prompt = ChatPromptTemplate.from_messages([
    ("system", system_prompt),
    ("human", "{question}")
])

chain = prompt | llm | StrOutputParser()

# Sidebar
with st.sidebar:
    st.title("💡 Suggested Questions")
    st.markdown("Click any question below:")
    
    for question in PREDEFINED_QUESTIONS:
        if st.button(question, key=question):
            st.session_state.selected_question = question

    st.markdown("---")
    st.markdown("### About")
    st.markdown("""
    **TechPulse AI** is a Generative AI chatbot built with:
    - Streamlit
    - LangChain
    - Groq (Llama 3.1)
    
    Created as a college project.
    """)

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Handle predefined question click
if "selected_question" in st.session_state:
    user_question = st.session_state.selected_question
    del st.session_state.selected_question
    
    st.session_state.messages.append({"role": "user", "content": user_question})
    
    with st.spinner("Thinking..."):
        response = chain.invoke({"question": user_question})
    
    st.session_state.messages.append({"role": "assistant", "content": response})

# Display chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Chat input
if prompt_input := st.chat_input("Ask me anything about technology..."):
    st.session_state.messages.append({"role": "user", "content": prompt_input})
    
    with st.chat_message("user"):
        st.markdown(prompt_input)
    
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            response = chain.invoke({"question": prompt_input})
            st.markdown(response)
    
    st.session_state.messages.append({"role": "assistant", "content": response})
