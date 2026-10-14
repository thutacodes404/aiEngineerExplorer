import os

from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"),
                base_url="https://api.groq.com/openai/v1")


def get_response(prompt):

    response = client.responses.create(
        model="openai/gpt-oss-20b",
        input=prompt
    )
    return response.output_text

def get_response_dual(system_prompt, user_prompt):
  # Assign the role and content for each message
  messages = [{"role": 'system', "content": system_prompt},
      		  {"role": 'user', "content": user_prompt}]  
  response = client.chat.completions.create(
      model="openai/gpt-oss-20b", messages= messages, temperature=0)
  
  return response.choices[0].message.content
