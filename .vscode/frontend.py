import streamlit as st
from dotenv import load_dotenv
from langchain.prompts import PromptTemplate
from langchain_groq import ChatGroq

load_dotenv()

#ui title

st.set_page_config(page_title="Chat Bot", layout="centered")
st.title("Gen Ai Project")
st.markdown("Ask a Question")

#user input

User_Question=st.text_input("Ask a Question")
if st.button("Get Answer") and User_Question.strip():
    with st.spinner("Fetting your Answer..."):
        text="""You are a Tollywood Fancy chatbot.always reply with Tollywood dialogue.
        {Question}"""

        prompt=PromptTemplate(
        input_variable=["Question"],
        template=text )

        llm=ChatGroq(model="deepseek-r1-distill-llama-70b")

        chain=prompt | llm

        try:
            result=chain.invoke({"Question":User_Question})
            st.success("here is your Answer")
            st.write(result.content)
        except Exception as e:
            st.error(f"Somthing Went Wrong: {str(e)}") 

else:
    st.caption("Powered by GROQ") 

