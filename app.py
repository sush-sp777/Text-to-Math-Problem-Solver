import streamlit as st
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

#streamlit app
st.set_page_config(page_title="Text To Math Problem Solver",page_icon="🦜",layout="centered")
st.title("Text to Math Problem Solver")
st.caption("Enter a math problem in plain English and the model will solve it step-by-step.")

groq_api_key=st.sidebar.text_input(label="GROQ_API_KEY",type="password")

if not groq_api_key:
    st.info("Please provide Groq API Key to continue")
    st.stop()
llm=ChatGroq(model="llama-3.1-8b-instant",groq_api_key=groq_api_key)

prompt=ChatPromptTemplate.from_template("""
You are a helpful assistant for solving mathemathical questions.
Logically arrive at the solution and provide a detailed explanation 
and display it point wise for the question below:\n
Question:\n {Question}
""")

parser=StrOutputParser()

chain=prompt|llm|parser

question=st.text_area("Enter the math problem:",height=150)

#solve button
if st.button("Solve"):
    if not question.strip():
        st.warning("Please enter the problem to solve.")
    else:
        with st.spinner("Solving..."):
            try:
                answer=chain.invoke({"Question":question})
            except Exception as e:
                st.error(f"Error:{e}")
                st.stop()
        st.markdown("### ✅ Solution")
        st.markdown(answer)