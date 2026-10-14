from openai import OpenAI
import os
from pydantic import BaseModel,Field

client = OpenAI(api_key=os.getenv("GROQ_API_KEY"),
                base_url="https://api.groq.com/openai/v1")

class SimilarMovie(BaseModel):
    title: str
    similarity_reason: str

class DetailedMovieRecommendation(BaseModel):
    title: str
    reason: str
    similar_movies: list[SimilarMovie]

# Create a structured response for movie recommendation
response = client.responses.parse(
    model="openai/gpt-oss-20b",
    instructions="You are a knowledgeable movie recommender.",
    input="Recommend a movie for someone who loved Inception and wants something mind-bending",
    text_format=DetailedMovieRecommendation
)

# Extract the parsed recommendation
recommendation = response.output_parsed

print(f"Title: {recommendation.title}")
print(f"\nSimilar movies:")
for movie in recommendation.similar_movies:
    print(f"- {movie.title}: {movie.similarity_reason}")