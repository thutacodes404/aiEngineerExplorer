import os

from pinecone import Pinecone, ServerlessSpec
import pinecone

pc=Pinecone(api_key=os.getenv("PINECONE_API_KEY"))

# pc.create_index(
#     name='mypinecone',
#     dimension=1536,
#     spec=ServerlessSpec(
#         cloud='aws',
#         region='us-east-1',
#     )
# )
pc.list_indexes()

index=pc.Index("mypinecone")

# check index stats
stats=index.describe_index_stats()

print(stats)

pc.delete_index("mypinecone")
print("Index deleted successfully.")


# Initialize the Pinecone client with your API key
pc = Pinecone(api_key=os.getenv)

# Connect to your index
index = pc.Index("datacamp-index")

# Print the index statistics
print(index.describe_index_stats())
ids = ['2', '5', '8']

# Fetch the vectors from the connected Pinecone index
fetched_vectors = index.fetch(ids=ids)

# Extract the metadata from each result in fetched_vectors
metadatas = [fetched_vectors['vectors'][id]['metadata'] for id in ids]
print(metadatas)

vector=[1.23313414241223]

# Retrieve the top three most similar records
query_result = index.query(
    vector=vector,
    top_k=3,

)
print(query_result)