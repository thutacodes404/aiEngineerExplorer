from openai import OpenAI
import os

client = OpenAI(api_key=os.getenv("GROQ_API_KEY"),
                base_url="https://api.groq.com/openai/v1")


# def get_response(prompt):

#     response = client.responses.create(
#         model="openai/gpt-oss-20b",
#         reasoning={'effort':'none'},
#         # max_output_tokens=60,
#         input=prompt,
#         instructions="Be concise"
#     )
#     return response.output_text

# prompt=""" what are the seven deadly sins """

# response=get_response(prompt)
# print(response)


def get_weather_response(prompt1):
        response=client.responses.create(
              model='openai/gpt-oss-20b',
              reasoning={'effort':'none'},
              tools=[{'type':'browser_search'}],
              input=prompt1,
            #   include=['web_search_call.action.sources']
        )
        return response


# for openai api call  

# Create a response with web search enabled and sources included
response = client.responses.create(
    model="gpt-5.4-mini",
    tools=[{"type": "web_search"}],
    input="What is the current stock price of Netflix?",
    include=["web_search_call.action.sources"]
)

# Extract and print sources from web search calls
for item in response.output:
    if item.type=='web_search_call':
        print(item.action.sources)
        
print(response.output_text)