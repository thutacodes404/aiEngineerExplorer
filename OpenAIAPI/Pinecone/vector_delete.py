
# Initialize the Pinecone client using your API key
import os

from pinecone import Pinecone
from pinecone import ServerlessSpec

pc = Pinecone(api_key=os.getenv("PINECONE_API_KEY"))

index = pc.Index('datacamp-index')

# Delete vectors
index.delete(ids=['3','4'])

# Retrieve metrics of the connected Pinecone index
print(index.describe_index_stats())