import streamlit as st
from gpt_chatbot import chatbot

st.title(":robot: Simple ChatBot")

with st.sidebar:
    openai_api_key = st.text_input("Your API Key", key="chatbot_api_key", type="password")
    "[New Window]()"
    "[Get an OpenAI API key](https://platform.openai.com/account/api-keys)"
    "[View the source code](https://github.com/aminbaghaeidev/Chatbot-using-openAI-API)"

if "messages" not in st.session_state:
    st.session_state["messages"] = [{"role": "assistant", "content": "How can I help you?"}]

for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

prompt = st.chat_input("Say Something...")
if prompt:
    if not openai_api_key:
        # st.info("Please add your OpenAI API key to continue.")
        # st.stop()
        openai_api_key = "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"


    
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)
    with st.spinner("Generating response..."):
        msg = chatbot(prompt, openai_api_key)
    st.session_state.messages.append({"role": "assistant", "content": msg})
    st.chat_message("assistant").write(msg)
