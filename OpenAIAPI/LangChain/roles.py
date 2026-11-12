from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
import os

llm = ChatOpenAI(
    api_key=os.getenv("GROQ_API_KEY"),
    base_url="https://api.groq.com/openai/v1",
    model="openai/gpt-oss-20b"
)

template = ChatPromptTemplate.from_messages([
    ("system", "You are a calculator that responds to math."),
    ("human", "Answer this math: what is ten plus ten divided by 5"),
    ("ai", "10 + 10 / 5 = 12"),
    ("human", "Answer this math question: {question}")
])

chain = template | llm

response = chain.invoke({
    "question": "What is five times five squared?"
})

print(response.content)