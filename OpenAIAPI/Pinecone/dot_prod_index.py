
# Initialize the Pinecone client with your API key
import os

from pinecone import Pinecone
from pinecone import ServerlessSpec
    
pc = Pinecone(api_key=os.getenv("PINECONE_API_KEY"))

# Create an index that uses the dot product distance metric
pc.create_index(
    name="dotproduct-index",
    dimension=1536,
    matrix='dotproduct',
    spec=ServerlessSpec(
        cloud='aws',
        region='us-east-1'
    )
)

# Print a list of your indexes
print(pc.list_indexes())