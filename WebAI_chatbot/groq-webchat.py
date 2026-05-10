import streamlit as st
from groq import Groq
from dotenv import load_dotenv
import os

# Load API key
load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

# Streamlit page setup
st.set_page_config(
    page_title="Groq AI Chat",
    page_icon="🤖"
)

st.title("🤖 Free Groq AI Sajida's Chatbot")

# Chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display old messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

# Chat input
prompt = st.chat_input("Ask something...")

if prompt:

    # Save user message
    st.session_state.messages.append(
        {"role": "user", "content": prompt}
    )

    # Show user message
    with st.chat_message("user"):
        st.write(prompt)

    # Get AI response
    with st.chat_message("assistant"):

        with st.spinner("Thinking..."):

            response = client.chat.completions.create(
                model="llama-3.1-8b-instant", 
                messages=st.session_state.messages
            )

            reply = response.choices[0].message.content

            st.write(reply)

    # Save assistant reply
    st.session_state.messages.append(
        {"role": "assistant", "content": reply}
    )