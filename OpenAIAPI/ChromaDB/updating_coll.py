import chromadb
import os
from chromadb.utils import embedding_functions

client=chromadb.PersistentClient(path='../stroage/chroma')

collection=client.get_collection(
    name='recommendation',
    embedding_function=embedding_functions.OpenAIEmbeddingFunction(
        model_name='sentence-transformers/all-MiniLM-L6-v2',
        api_key=os.getenv("GROQ_API_KEY")
    )
)

# update the documents in the collection, use two
collection.update(
    ids=["doc1", "doc2"],
    documents=['Hello World', 'Hello Universe'],
)

# update if id exists, else insert new document
collection.upsert(
    ids=['id-2','id-67'],
    documents=['Hello Sonnet', 'Hello Milkey Way'],
)

# peek the collection 
collection.peak()

# count the number of documents in the collection
collection.count()

# delete the documents from the collection and reset the collection
collection.delete(
    ids=['id-2','id-67']
)
collection.reset()
