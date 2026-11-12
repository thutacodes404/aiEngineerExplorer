import pandas as pd
import numpy as np
import os
from uuid import uuid4
from openai import OpenAI
from sentence_transformers import SentenceTransformer

client = OpenAI(
    api_key=os.getenv("GROQ_API_KEY"),
    base_url="https://api.groq.com/openai/v1"
)
df = pd.read_csv("./datasets/squad_dataset.csv")
print(df.head(4))
batch_limit = 100

for i in range(0, len(df), batch_limit):
    batch = df.iloc[i:i + batch_limit]
    metadatas = [
        {
            "text_id": row["id"],
            "text": row["text"],
            "title": row["title"],
        }
        for _, row in batch.iterrows()
    ]
    texts = batch["text"].tolist()
    ids = [str(uuid4()) for _ in range(len(texts))]

    # embedding code goes here

embedding_model = SentenceTransformer(
    "sentence-transformers/all-MiniLM-L6-v2"
)