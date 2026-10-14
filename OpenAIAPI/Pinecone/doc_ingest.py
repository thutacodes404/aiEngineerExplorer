import pandas as pd 
import numpy as np
import os
import _osx_support
from uuid import uuid4
from openai import OpenAI

client = OpenAI(api_key=os.getenv("GROQ_API_KEY"),
                base_url="https://api.groq.com/openai/v1")


df=pd.read_csv('./datasets/squad_dataset.csv')
print(df.head(4))

# start ingesting
batch_limit=100

for batch in np.array.split(df,len(df)/batch_limit):
    metadatas=[{
        'text_id': row['id'],
        "text": row['text'],
        'title': row['title'],
    } for _, row in batch.iterrows()]
    texts=batch['text'].tolist()
    ids=[str(uuid4()) for _ in range(len(texts))]
    response=client.embeddings.create(input=texts, model="text-embedding-3-small")
    embeds=[np.array(x.embedding) for x in response.data]