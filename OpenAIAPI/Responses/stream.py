from openai import OpenAI
import os
from pydantic import BaseModel,Field

client = OpenAI(api_key=os.getenv("GROQ_API_KEY"),
                base_url="https://api.groq.com/openai/v1")



prompt = "List the core ingredients to make classic egg pasta pasta in a single line."

# Open a connection for a streaming request
with client.responses.create(model="openai/gpt-oss-20b", input=prompt, stream=True) as stream:
    current_text = ""

    # Complete the output text streaming
    for event in stream:
        if event.type == "response.output_text.delta":
            current_text += event.delta
            print(current_text)