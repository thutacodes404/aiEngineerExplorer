from openai import OpenAI
import os
from pydantic import BaseModel,Field

client = OpenAI(api_key=os.getenv("GROQ_API_KEY"),
                base_url="https://api.groq.com/openai/v1")


prompt = "Explain how to read a weather forecast in one sentence for a beginner hiker."

with client.responses.create(model="openai/gpt-oss-20b", input=prompt, stream=True) as stream:
    current_text = ""

    for event in stream:
        # Find response created events
        if event.type == "response.created":
            print("Forecast generation started...\n")

        # Find output text completed events
        elif event.type == "response.output_text.done":
            print("\n--- Forecast complete ---\n")

        # Find response completed events
        elif event.type == "response.completed":
            print(f"\nFull forecast:\n{current_text}")