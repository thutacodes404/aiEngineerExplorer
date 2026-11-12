from pinecone import Pinecone
import os
import pandas as pd
import numpy as np
from uuid import uuid4

from openai import OpenAI
from dotenv import load_dotenv
from sentence_transformers import SentenceTransformer


# =========================
# Load environment variables
# =========================
load_dotenv()


# =========================
# Groq LLM client
# =========================
client = OpenAI(
    api_key=os.getenv("GROQ_API_KEY"),
    base_url="https://api.groq.com/openai/v1"
)


# =========================
# Local embedding model
# =========================
embedding_model = SentenceTransformer(
    "sentence-transformers/all-MiniLM-L6-v2"
)


# =========================
# Pinecone
# =========================
pc = Pinecone(
    api_key=os.getenv("PINECONE_API_KEY")
)

index = pc.Index("sematci-search-datacamp")

namespace = "youtube_rag_dataset"


# =========================
# Document ingestion
# =========================
df = pd.read_csv("../datasets/youtube_rag_data.csv")

batch_limit = 100

num_batches = int(np.ceil(len(df) / batch_limit))

for batch in np.array_split(df, num_batches):
    metadatas = [
        {
            "text_id": int(row["id"]),
            "text": row["text"],
            "title": row["title"],
            "url": row["url"],
            "published": str(row["published"])
        }
        for _, row in batch.iterrows()
    ]
    texts = batch["text"].tolist()
    ids = [str(uuid4())for _ in range(len(texts))]

    # Create local embeddings
    embeddings = embedding_model.encode(
        texts,
        normalize_embeddings=True
    ).tolist()

    # Prepare Pinecone vectors
    vectors = [
        {
            "id": ids[i],
            "values": embeddings[i],
            "metadata": metadatas[i]
        }
        for i in range(len(texts))
    ]

    # IMPORTANT: store vectors in Pinecone
    index.upsert(
        vectors=vectors,
        namespace=namespace
    )

    print(f"Uploaded {len(vectors)} vectors")


# =========================
# Retrieval
# =========================
def retrieve(query, top_k, namespace, embedding_model):

    # Embed query using SAME model as documents
    query_embedding = embedding_model.encode(
        query,
        normalize_embeddings=True
    ).tolist()

    results = index.query(
        vector=query_embedding,
        top_k=top_k,
        namespace=namespace,
        include_metadata=True
    )

    retrieved_docs = []
    sources = []

    for match in results["matches"]:
        metadata = match["metadata"]
        retrieved_docs.append(
            metadata["text"]
        )
        sources.append(
            (
                metadata["title"],
                metadata["url"]
            )
        )
    return retrieved_docs, sources


# =========================
# Retrieve relevant documents
# =========================
query = "How to build next-level Q&A with OpenAI"

documents, sources = retrieve(
    query=query,
    top_k=3,
    namespace=namespace,
    embedding_model=embedding_model
)


# =========================
# Build RAG prompt
# =========================
def prompt_with_context_builder(query, docs):

    delimiter = "\n\n---\n\n"

    prompt_start = """Answer the question using only the context below.Context:"""
    prompt_end = f"""Question:{query}Answer:"""
    prompt = (
        prompt_start
        + delimiter.join(docs)
        + prompt_end
    )
    return prompt


# =========================
# Generate answer with Groq
# =========================
def question_answering(prompt, sources, chat_model):

    system_prompt = (
        "You are a helpful assistant. "
        "Answer questions using the provided context."
    )

    response = client.chat.completions.create(
        model=chat_model,
        messages=[
            {
                "role": "system",
                "content": system_prompt
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0
    )

    answer = response.choices[0].message.content.strip()

    answer += "\n\nSources:"

    for title, url in sources:
        answer += f"\n{title}: {url}"
    return answer


# =========================
# RAG
# =========================
context_prompt = prompt_with_context_builder(
    query,
    documents
)
answer = question_answering(
    context_prompt,
    sources,
    chat_model="openai/gpt-oss-20b"
)
print(answer)