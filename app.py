import streamlit as st
from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage, SystemMessage, AIMessage
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Page configuration
st.set_page_config(
    page_title="TechPulse AI - GenAI Chatbot",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for better look
st.markdown("""
<style>
    .stApp {
        background-color: #0f172a;
    }
    .main-header {
        font-size: 2.2rem;
        font-weight: 700;
        color: #38bdf8;
        margin-bottom: 0.2rem;
    }
    .sub-header {
        color: #94a3b8;
        font-size: 0.95rem;
        margin-bottom: 1.5rem;
    }
    .stButton > button {
        width: 100%;
        border-radius: 0.5rem;
        border: 1px solid #334155;
        background-color: #1e293b;
        color: #e2e8f0;
        text-align: left;
        padding: 0.6rem 0.9rem;
        font-size: 0.85rem;
    }
    .stButton > button:hover {
        border-color: #0ea5e9;
        background-color: #0c4a6e;
        color: #7dd3fc;
    }
    div[data-testid="stChatMessage"] {
        background-color: #1e293b;
        border-radius: 0.75rem;
        padding: 0.8rem;
        margin-bottom: 0.6rem;
    }
</style>
""", unsafe_allow_html=True)

# ====================== SYSTEM PROMPT ======================
SYSTEM_PROMPT = """You are TechPulse AI, a helpful, friendly and knowledgeable Generative AI assistant specialized in Technology, Programming, Artificial Intelligence, and Computer Science.

### Guidelines:
1. You can answer ANY question related to technology, programming, AI, software development, cloud, cybersecurity, data science, etc.
2. When the question matches one of the topics in the PREDEFINED KNOWLEDGE below, prefer to use that information and expand on it if needed.
3. For questions outside pure technology (sports, politics, personal life, medical advice, etc.), politely say that you are specialized in technology topics and ask the user to ask a tech-related question.
4. Keep answers clear, well-structured, and easy to understand.
5. Use simple language. Prefer answers under 180 words unless the user asks for more detail.

=== PREDEFINED KNOWLEDGE (use this as primary source when relevant) ===

1. Artificial Intelligence (AI): Simulation of human intelligence in machines. Includes Machine Learning, Deep Learning, NLP, and Computer Vision.

2. Machine Learning: Subset of AI that enables systems to learn from data without being explicitly programmed. Types: Supervised, Unsupervised, Reinforcement Learning.

3. MERN Stack: MongoDB + Express.js + React.js + Node.js. A popular full-stack JavaScript framework for building modern web applications.

4. Generative AI: AI models that can create new content (text, images, code, music, videos). Examples: ChatGPT, DALL-E, Midjourney, Stable Diffusion. Based on Large Language Models.

5. Cloud Computing: Delivery of computing services over the internet. Major providers: AWS, Azure, Google Cloud. Benefits: scalability, cost efficiency, high availability.

6. Cybersecurity: Practice of protecting systems, networks and data from digital attacks. Common threats: malware, phishing, ransomware, DDoS.

7. Blockchain: Distributed and immutable digital ledger. Foundation of cryptocurrencies (Bitcoin, Ethereum) and used in supply chain, healthcare, etc.

8. AI vs ML vs Deep Learning:
   - AI → Broad concept of machines mimicking human intelligence
   - Machine Learning → Subset of AI that learns from data
   - Deep Learning → Subset of ML using multi-layer neural networks

9. React.js: Popular JavaScript library for building user interfaces using components and Virtual DOM.

10. Node.js: JavaScript runtime that allows running JS on the server. Event-driven and non-blocking.

11. Large Language Models (LLMs): Advanced AI models trained on huge text data that can understand and generate human-like language (GPT, Claude, Llama, Gemini, etc.).

12. Prompt Engineering: The skill of writing effective prompts to get the best results from Generative AI models.

=== END OF PREDEFINED KNOWLEDGE ===

Always be helpful and encouraging to students learning technology.
"""

# Predefined questions for the sidebar
PREDEFINED_QUESTIONS = [
    "What is Artificial Intelligence (AI)?",
    "What is Machine Learning?",
    "What is the MERN Stack?",
    "What is Generative AI?",
    "What is Cloud Computing?",
    "What is Cybersecurity?",
    "Difference between AI, ML, and Deep Learning?",
    "What are Large Language Models (LLMs)?",
    "What is React.js?",
    "What is Prompt Engineering?",
    "What is Blockchain?",
    "What is Node.js?"
]

# ====================== INITIALIZE MODEL ======================
@st.cache_resource
def get_llm():
    api_key = os.getenv("GROQ_API_KEY")
    if not api_key:
        return None
    return ChatGroq(
        model="openai/gpt-oss-20b",   # Free & currently available model on Groq
        temperature=0.6,
        max_tokens=500,
        groq_api_key=api_key
    )

llm = get_llm()

# ====================== SESSION STATE ======================
if "messages" not in st.session_state:
    st.session_state.messages = [
        {
            "role": "assistant",
            "content": "Hello! 👋 I am **TechPulse AI**, your GenAI assistant.\n\nI can answer **any technology-related question** (AI, Programming, Web Development, Cloud, Cybersecurity, etc.).\n\nYou can also click the **Suggested Questions** on the left for quick answers.\n\nAsk me anything related to technology!"
        }
    ]

# ====================== SIDEBAR ======================
with st.sidebar:
    st.markdown("## 🤖 TechPulse AI")
    st.markdown("**GenAI Chatbot** using LangChain + Groq")
    st.markdown("---")
    st.markdown("### 💡 Suggested Questions")
    st.caption("Click any question to ask instantly")

    for question in PREDEFINED_QUESTIONS:
        if st.button(question, key=question):
            st.session_state.pending_question = question

    st.markdown("---")
    st.markdown("### About")
    st.caption("College GenAI Project")
    st.caption("Built with Streamlit + LangChain + Groq")
    
    if st.button("🗑️ Clear Chat"):
        st.session_state.messages = [
            {
                "role": "assistant",
                "content": "Chat cleared! How can I help you with technology topics?"
            }
        ]
        st.rerun()

# ====================== MAIN AREA ======================
st.markdown('<p class="main-header">🤖 TechPulse AI</p>', unsafe_allow_html=True)
st.markdown('<p class="sub-header">Generative AI Chatbot • Powered by LangChain + Groq</p>', unsafe_allow_html=True)

# Check API key
if llm is None:
    st.error("⚠️ GROQ_API_KEY not found! Please create a `.env` file and add your Groq API key.")
    st.code("GROQ_API_KEY=your_groq_api_key_here", language="bash")
    st.info("Get a free Groq API key from: https://console.groq.com/keys")
    st.stop()

# Display chat messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Handle pending question from sidebar buttons
if "pending_question" in st.session_state:
    prompt = st.session_state.pending_question
    del st.session_state.pending_question
else:
    prompt = st.chat_input("Ask a technology question...")

# Process user input
if prompt:
    # Add user message
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Generate AI response
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            try:
                # Build message history for LangChain
                langchain_messages = [SystemMessage(content=SYSTEM_PROMPT)]
                
                # Add previous conversation (limit to last 6 messages for context)
                for msg in st.session_state.messages[-7:-1]:
                    if msg["role"] == "user":
                        langchain_messages.append(HumanMessage(content=msg["content"]))
                    else:
                        langchain_messages.append(AIMessage(content=msg["content"]))
                
                # Current question
                langchain_messages.append(HumanMessage(content=prompt))

                # Call the model
                response = llm.invoke(langchain_messages)
                answer = response.content

                st.markdown(answer)
                st.session_state.messages.append({"role": "assistant", "content": answer})

            except Exception as e:
                error_msg = f"⚠️ Error: {str(e)}"
                st.error(error_msg)
                st.session_state.messages.append({"role": "assistant", "content": error_msg})
