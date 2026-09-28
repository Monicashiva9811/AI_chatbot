import os
import streamlit as st
from dotenv import load_dotenv
from google import genai

load_dotenv()

st.set_page_config(page_title="Gemini AI Chatbot", page_icon="🤖")

st.title("🤖 Gemini AI Chatbot")
st.caption("Powered by Gemini 2.5 Flash")

# --- Client setup ---
@st.cache_resource
def get_client():
    return genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

client = get_client()

# --- Chat history in session state ---
if "messages" not in st.session_state:
    st.session_state.messages = []

# --- Sidebar controls ---
with st.sidebar:
    st.header("Settings")
    if st.button("🗑️ Clear chat"):
        st.session_state.messages = []
        st.rerun()

# --- Render past messages ---
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# --- Chat input ---
user_input = st.chat_input("Type your message...")

if user_input:
    # Show user message
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    # Get Gemini response
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            try:
                response = client.models.generate_content(
                    model="gemini-2.5-flash",
                    contents=user_input
                )
                reply = response.text
            except Exception as e:
                reply = f"⚠️ Error: {e}"
            st.markdown(reply)

    st.session_state.messages.append({"role": "assistant", "content": reply})