import numpy as np
from openai import OpenAI
from scipy import spatial
from scipy.spatial import distance
import os
import openai
from sentence_transformers import SentenceTransformer

client = OpenAI(api_key=os.getenv("GROQ_API_KEY"),
                base_url="https://api.groq.com/openai/v1")

embedding_model = SentenceTransformer("all-MiniLM-L6-v2")


articles = [
    {
        "headline": "Economic Growth Continues Amid Global Uncertainty",
        "topic": "Business",
        "keywords": [
            "economy",
            "business",
            "finance",
            "growth",
            "market"
        ]
    },
    {
        "headline": "1.5 Billion Tune-in to the World Cup Final",
        "topic": "Sport",
        "keywords": [
            "soccer",
            "football",
            "world cup",
            "sports",
            "television",
            "audience"
        ]
    },
    {
        "headline": "NVIDIA Unveils Next-Generation GPUs for AI",
        "topic": "Tech",
        "keywords": [
            "nvidia",
            "gpu",
            "ai",
            "artificial intelligence",
            "hardware",
            "chips"
        ]
    },
    {
        "headline": "OpenAI Releases a New Generation of AI Models",
        "topic": "Tech",
        "keywords": [
            "openai",
            "ai",
            "llm",
            "artificial intelligence",
            "machine learning",
            "models"
        ]
    },
    {
        "headline": "Global Stock Markets Rise as Investors Expect Strong Growth",
        "topic": "Business",
        "keywords": [
            "stocks",
            "market",
            "investment",
            "finance",
            "economy",
            "growth"
        ]
    },
    {
        "headline": "Premier League Club Announces Major New Signing",
        "topic": "Sport",
        "keywords": [
            "football",
            "soccer",
            "premier league",
            "transfer",
            "player",
            "club"
        ]
    },
    {
        "headline": "Apple Introduces a More Powerful MacBook Processor",
        "topic": "Tech",
        "keywords": [
            "apple",
            "macbook",
            "processor",
            "chip",
            "computer",
            "technology"
        ]
    },
    {
        "headline": "Bitcoin Surges as Institutional Investors Increase Their Holdings",
        "topic": "Business",
        "keywords": [
            "bitcoin",
            "crypto",
            "cryptocurrency",
            "investment",
            "finance",
            "market"
        ]
    },
    {
        "headline": "Scientists Develop a More Efficient Solar Energy Technology",
        "topic": "Science",
        "keywords": [
            "science",
            "solar",
            "energy",
            "technology",
            "climate",
            "research"
        ]
    },
    {
        "headline": "Google Expands Its AI Infrastructure to Support Growing Demand",
        "topic": "Tech",
        "keywords": [
            "google",
            "ai",
            "data center",
            "infrastructure",
            "machine learning",
            "computing"
        ]
    }
]

user_history=[
    {'headline':'How NIVIDIA GPUS could decide who wins the AI race',
     'topic':'tech',
     'keywords':['ai','business','computers']},
     {'headline':'Tech Giant Buys 49% Stake in AI startup',
      'topic':'tech',
      'keywords':['business','AI']}
]


def create_article_text(article):
    return f"""Headline :{article['headline']}
                Topic:{article['topic']}
                Keywords:{','.join(article['keywords'])}"""

history_texts=[create_article_text(article) for article in user_history]

# alternative using free llm
def create_embeddings(texts):
    response = embedding_model.encode(texts)
    response_dict = {
        "data": [
            {"embedding": embedding.tolist()}
            for embedding in response
        ]
    }
    return [data["embedding"] for data in response_dict["data"]]

history_embeddings=create_embeddings(history_texts)

mean_history_embeddings = np.mean(
    history_embeddings,
    axis=0
)

articles_filtered = [
    article for article in articles
    if article not in user_history
]

article_text = [
    create_article_text(article)
    for article in articles_filtered
]

article_embeddings = create_embeddings(article_text)

def find_n_closest(query_vector, embeddings, n=3):
    distances = []
    for index, embedding in enumerate(embeddings):
        dist = distance.cosine(query_vector, embedding)
        distances.append({
            "distance": dist,
            "index": index
        })
    distance_sorted = sorted(
        distances,
        key=lambda x: x["distance"]
    )

    return distance_sorted[:n]

hits=find_n_closest(mean_history_embeddings,article_embeddings)

for hit in hits:
    article=articles_filtered[hit['index']]
    print(article['headline'])