from langchain_huggingface import ChatHuggingFace,HuggingFaceEndpoint
from langchain_core.messages import SystemMessage,HumanMessage,AIMessage
from dotenv import load_dotenv
import streamlit as st

load_dotenv()

llm=HuggingFaceEndpoint(repo_id="Qwen/Qwen3.8-27B:ovhcloud",task="text-generation",max_new_tokens=1024)
model=ChatHuggingFace(llm=llm)

st.header("Akshay's chatbot")

if "messages" not in st.session_state:
    st.session_state.messages=[
        SystemMessage(content="You are a helpful assistant")
    ]

for message in st.session_state.messages:
     if type(message)==HumanMessage:
        with st.chat_message("user"):
            st.write(message.content)
     elif type(message)==AIMessage:
         with st.chat_message("assistant"):
             st.write(message.content)

user_input=st.chat_input("type your message ")

if user_input:
    st.session_state.messages.append(HumanMessage(content=user_input))

    result=model.invoke(st.session_state.messages)
    st.session_state.messages.append(AIMessage(content=result.content))

    st.rerun()
if st.button("🗑️ Clear Chat"):
    st.session_state.messages = [
        SystemMessage(content="You are a helpful assistant")
    ]
    st.rerun()