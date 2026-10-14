import os
from openai import OpenAI
from pinecone import Pinecone
from pinecone import ServerlessSpec
    
# pinecone api
pc=Pinecone(api_key=os.getenv)

# open ai api
client = OpenAI(api_key=os.getenv("GROQ_API_KEY"),
                base_url="https://api.groq.com/openai/v1")

pc.create_index(
    name='sematic-search-index',
    dimension=1536,
    spec=ServerlessSpec(
        cloud='aws',
        region='us-east-1'
    )
)

index=pc.Index('sematic-search-index')