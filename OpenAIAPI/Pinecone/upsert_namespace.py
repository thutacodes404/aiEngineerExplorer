import os

from pinecone import Pinecone
from pinecone import ServerlessSpec

pc = Pinecone(api_key=os.getenv("PINECONE_API_KEY"))

index=pc.Index("dotproduct-index")
vectors=[
    {
        "id": "1",
        "values": [0.1, 0.2, 0.3],
        "metadata": {"genre": "comedy", "year": "2021"}
    },
    {
        "id": "2",
        "values": [0.4, 0.5, 0.6],
        "metadata": {"genre": "action", "year": "2022"}
    },
]
namespace1="namespace1"
namespace2="namespace2"

index.upsert(
    vectors=vectors,
    namespace='namespace1'
)
index.upsert(
    vectors=vectors,
    namespace='namespace2'
)

print(index.describe_index_stats())