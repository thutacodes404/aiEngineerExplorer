from openai import OpenAI
from scipy import spatial
from scipy.spatial import distance
import os
import openai
from sentence_transformers import SentenceTransformer

client = OpenAI(api_key=os.getenv("GROQ_API_KEY"),
                base_url="https://api.groq.com/openai/v1")

topics=[
    {'label':'Tech'},
    {'label':'Business'},
    {'label':'Sport'},
    {'label':'Politics'},
    {'label':'Health'},
    {'label':'Science'},
    {'label':'Entertainment'},
    {'label':'Travel'},
    {'label':'Food'},
    {'label':'Education'}
]

article ={'headline': 'How NVIDIA GPUs Could Decide Who Wins the AI Race',
          'keywords': ['ai','business','computers']}


def create_article_text(article):
    return f"Headline: {article['headline']}\nKeywords: {', '.join(article['keywords'])}"

article_text = create_article_text(article)

def find_closest(query_vector,embeddings):
    distances=[]
    for index, embedding in enumerate(embeddings):
        dist=distance.cosine(query_vector,embedding)
        distances.append({
            "distance":dist,
            "index":index
        })
        return sorted(distances,key=lambda x:x["distance"])

closest=find_closest(article_embeddings ,class_embeddings)