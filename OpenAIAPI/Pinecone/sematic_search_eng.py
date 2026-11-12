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

query='To whom did the Virgin Mary allegedly appear in 1858 in Lourdes France?'

query_response=client.embeddings.create(
    input=query,
    model='text-embedding-small')

query_emb=query.response.data[0].embedding

retrive_doc=index.query(
    vector=query_emb,
    top_k=3,
    namespace=namespace,
    include_metadata=True
)

for result in retrive_doc['matches']:
    print(f"{round(result['score'],2)}:{result['metadata']['text']}")