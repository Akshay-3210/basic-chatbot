from langchain_huggingface import ChatHuggingFace,HuggingFaceEndpoint
from dotenv import load_dotenv
import streamlit as st

load_dotenv()

llm=HuggingFaceEndpoint(repo_id="Qwen/Qwen3.8-27B:ovhcloud",task="text-generation",max_new_tokens=1024)
model=ChatHuggingFace(llm=llm)

st.header("Akshay's chatbot")

if "messages" not in st.session_state:
    st.session_state.messages=[]

for message in st.session_state.messages:
     with st.chat_message(message["role"]):
        st.write(message["content"])

user_input=st.chat_input("type your message ")

if user_input:
    st.session_state.messages.append({"role":"user","content":user_input})

    query=""
    for message in st.session_state.messages:
        if message["role"]=="user":
            query=query+"user: "
        else:
            query=query+"AI: "
        query=query+message["content"]
    query=query+"\n"+user_input

    result=model.invoke(query)
    st.session_state.messages.append({"role":"assistant","content":result.content})

    st.rerun()
if st.button("🗑️ Clear Chat"):
    st.session_state.messages = []
    st.rerun()