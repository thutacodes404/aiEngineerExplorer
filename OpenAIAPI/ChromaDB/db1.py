import os
from openai import OpenAI

client = OpenAI(
    api_key=os.getenv("GROQ_API_KEY"),
    base_url="https://api.groq.com/openai/v1"
)
import chromadb
from chromadb.utils.embedding_functions import OpenAIEmbeddingFunction
client=chromadb.PersistentClient(path='../stroage/chroma')

collection=client.create_collection(
    name='recommendation',
    embedding_function=OpenAIEmbeddingFunction(
        model_name='text-embedding-3-small',
        api_key=os.getenv("GROQ_API_KEY")
    )
)
# add the documents and ID to the collection
collection.add(
    documents=[
        "The quick brown fox jumps over the lazy dog.",
        "A journey of a thousand miles begins with a single step.",
        "To be or not to be, that is the question.",
        "All that glitters is not gold.",
        "I think, therefore I am."
    ],
    ids=["doc1", "doc2", "doc3", "doc4", "doc5"]
)

client.list_collections()
collection.peak()
print("No of documents in the collection:", collection.count())
print('First 5 documents in the collection:', collection.peek(5))