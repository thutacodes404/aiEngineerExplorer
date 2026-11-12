# Initialize the Pinecone client
pc = Pinecone(api_key="pcsk_6Jtuws_3gzsJkKbcY2osxZds8UN5o1LUfdvM5JmuaAhs8edrAmdCZ6HDwaNAPPCP47gzos")
index = pc.Index('pinecone-datacamp')

query = "What is in front of the Notre Dame Main Building?"

# Create the query vector
query_response = client.embeddings.create(
    input=query,
    model="text-embedding-3-small"
)
query_emb = query_response.data[0].embedding

# Query the index and retrieve the top five most similar vectors
retrieved_docs = index.query(vector=query_emb,top_k=5,namespace='squad_dataset')

for result in retrieved_docs['matches']:
    print(f"{result['id']}: {round(result['score'], 2)}")
    print('\n')