import streamlit as st
from streamlit.report_thread import REPORT_CONTEXT_ATTR_NAME
from threading import current_thread
from typing import Dict

class SessionState:
    def __init__(self, **kwargs):
        """A new SessionState object."""
        for key, val in kwargs.items():
            setattr(self, key, val)

def get_session():
    ctx = getattr(current_thread(), REPORT_CONTEXT_ATTR_NAME, None)
    session = getattr(ctx, 'session', None)
    return session

def get_state() -> SessionState:
    session = get_session()
    if not hasattr(session, '_custom_session_state'):
        session._custom_session_state = SessionState()
    return session._custom_session_state

state = get_state()

st.title("LogGPT: Interactive Log Analyser")

uploaded_file = st.file_uploader("Upload a log file", type=("json"))

prompt = st.text_input(
    "Ask something about your logs to start analyzing",
    placeholder="Can you give me a short summary?", disabled=not uploaded_file)

if 'messages' not in state:
    state.messages = [{"role": "assistant", "content": "How can I help you?"}]

if st.button('Start interacting'):
    for msg in state.messages:
        st.chat_message(msg["role"]).write(msg["content"])

    if uploaded_file and prompt:
        with st.spinner("Wait for the response"):
            context_text = get_context(prompt)
            response = conversation.predict(input=context_text+prompt)
            st.write("### Answer")
            st.write(response)

        if prompt := st.chat_input():
            state.messages.append({"role": "user", "content": prompt})
            st.chat_message("user").write(prompt)

            # response = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=state.messages)
            # state.messages.append(msg)
            # st.chat_message("assistant").write(msg.content)
