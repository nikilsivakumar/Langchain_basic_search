##Integrate code to OpenAI API
#documentstion from Open ai website

import os
from constants import openai_key
#from langchain.llms import OpenAI
from langchain_openai import OpenAI

import streamlit as st

os.environ["OPENAI_API_KEY"]=openai_key

#init streamlit framework

st.title('Langchain Demo with OpenAI API')
input_text = st.text_input("Search")

#OpenAI LLMs
llm = OpenAI(temperature=0.8)


if input_text:
    st.write(llm(input_text))