from openai import OpenAI

import os

client = OpenAI(api_key=os.getenv("GROQ_API_KEY"),
                base_url="https://api.groq.com/openai/v1")

response1=client.responses.create(
    model='openai/gpt-oss-20b',
    input='hello my name is Kyaw Thuta Oo'
)
print(response1.id)
print(response1.output_text)

response2=client.responses.create(
    model='openai/gpt-oss-20b',
    input='what is my name again',
    previous_response_id=response1.id
)

print(response2.id)
print(response2.output_text)

response3=client.responses.create(
    model='openai/gpt-oss-20b',
    input='summarize the conversation',
    previous_response_id=response2.id,
)
print(response3.id)
print(response3.output_text)



# Loop through the output items
for item in response1.output:
    # Check for reasoning items
    if item.type == 'reasoning':
        print('Found reasoning item')
    
    # Check for message items and extract text
    if item.type == 'message':
        message_text = item.content[0].text
        print(message_text)



# Loop through each item in the response output
for item in response.output:
    # Check if the item is a reasoning item
    if item.type == 'reasoning':
        if item.summary:
            print(f"Reasoning: {item.summary[0]}")
        else:
            print("No reasoning summary found.")   
    
    # Check if the item is a message item
    if item.type == 'message':
        print(f"Assistant: {item.content[0].text}")