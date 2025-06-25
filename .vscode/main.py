from dotenv import load_dotenv
load_dotenv()
import os
print(os.environ["GROQ_API_KEY"])
#chatbot basic steps
#1.take user input
user_input=input("Enter your Question:")

#2.Convert into prompt
from langchain.prompts import PromptTemplate
text="""You are a Tollywood Fancy chatbot.always reply with Tollywood dialogue.
{Question}"""
prompt=PromptTemplate(
    input_variable=["Question"],
    template=text 
)

#3.Make LLM call
#from langchain_openai import ChatOpenAI
from langchain_groq import ChatGroq
llm=ChatGroq(model="deepseek-r1-distill-llama-70b")
#create chain
chain=prompt | llm

#4.Response
result=chain.invoke({"Question":user_input})
print(result.content)