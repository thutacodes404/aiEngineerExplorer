import chromadb
from chromadb.utils.embedding_functions import SentenceTransformerEmbeddingFunction


# 1. Embedding model
embedding_function = SentenceTransformerEmbeddingFunction(
    model_name="all-MiniLM-L6-v2"
)


# 2. Connect to existing ChromaDB
client = chromadb.PersistentClient(
    path="./storage/chroma"
)


# 3. Connect to existing collection
collection = client.get_collection(
    name="recommendation",
    embedding_function=embedding_function
)


# 4. Search
query = "What is used for vector search?"

results = collection.query(
    query_texts=[query],
    n_results=3
)


# 5. Display results
print("\nQuery:")
print(query)

print("\nTop results:")

for document in results["documents"][0]:
    print("-", document)