import os

from pinecone import Pinecone 
import itertools
pc=Pinecone(api_key=os.getenv("PINECONE_API_KEY"),
            pool_threads=30)

# create chunk function
def chunk(iterable,batch_size=100):
    it=iter(iterable)
    chunk=tuple(itertools.islice(it,batch_size))
    while chunk:
        yield chunk
        chunk=tuple(itertools.islice(it,batch_size))

with pc.Index('datacamp-index',pool_threads=30) as index:
    async_results=[index.upsert(vectors=chunk,async_req=True)
                   for chunk in chunk(vectors,batch_size=1000)]


index = pc.Index('datacamp-index')
# Upsert vectors in batches of 100
for chunk in chunk(vectors,batch_size=100):
    index.upsert(vectors=chunk) 

# Retrieve statistics of the connected Pinecone index
print(index.describe_index_stats())