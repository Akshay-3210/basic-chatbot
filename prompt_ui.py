from langchain_huggingface import ChatHuggingFace,HuggingFaceEndpoint
from dotenv import load_dotenv
import streamlit as st

load_dotenv()

st.header("research tool")
user_input=st.text_input("enter your prompt ")

llm=HuggingFaceEndpoint(repo_id="Qwen/Qwen3.8-27B:ovhcloud",task="text-generation",temperature=0)
model=ChatHuggingFace(llm=llm)
if st.button("summarize"):
    result=model.invoke(user_input)
    st.text(result.content)