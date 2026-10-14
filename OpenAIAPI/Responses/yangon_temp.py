from OpenAIAPI.Responses.api_connection import get_weather_response

prompt= """what is the current temperature in yangon"""

response=get_weather_response(prompt)
print(response)


for item in response.output:
    if item.type=='browser_search_call':
        print(item)