from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
import os
from langchain_core.output_parsers import StrOutputParser


llm=ChatOpenAI(
    api_key=os.getenv("GROQ_API_KEY"),
    base_url="https://api.groq.com/openai/v1",
    model='qwen/qwen3.8-27b'
)


destination_prompt=PromptTemplate(
    input_variables=['destination'],
    template="I want to go to {destination} for a trip."
)

activity_prompt=PromptTemplate(
    input_variables=['activities'],
    template="I only have one day . What {activities} can i do in a day , iternary from your top "
)

llm_chain = (
    {
        "activities":
            destination_prompt
            | llm
            | StrOutputParser()
    }
    | activity_prompt
    | llm
    | StrOutputParser()
    )


result=llm_chain.invoke({'destination':'Germany'})

print(result)
