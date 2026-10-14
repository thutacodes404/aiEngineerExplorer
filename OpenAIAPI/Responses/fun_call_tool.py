import json

from openai import OpenAI
import os

client = OpenAI(api_key=os.getenv("GROQ_API_KEY"),
                base_url="https://api.groq.com/openai/v1")

tools = [
    {
        "type": "function",
        "name": "convert_currency",
        "description": "Convert the amount from one currency to another using real-time exchange rates.",
        "parameters": {
            "type": "object",

            "properties": {
                "amount": {
                    "type": "number",
                    "description": "The amount of money to convert."
                },
                "from_currency": {
                    "type": "string",
                    "description": 'The source currency, e.g. "USD".'
                },
                "to_currency": {
                    "type": "string",
                    "description": 'The target currency, e.g. "MMK".'
                }
            },

            "required": [
                "amount",
                "from_currency",
                "to_currency"
            ],

            "additionalProperties": False
        }
    }
]

messages=[
      {'role':'system','content':'you are the customer chat bot from currency exchange department of a Bank'},
      {'role':'user','content':'How much is 100$ in mmk?'}      
      ]

def curr_exchange():
        response=client.responses.create(
            model='openai/gpt-oss-20b',
            input=messages,
            tools=tools
        )
        
        return response

response=curr_exchange()
messages+=response.output

for item in response.output:
    if item.type=='function_call':
          if item.name=='convert_currency':
                currency_result=curr_exchange(**json.loads(item.arguments))
                messages.append({
                      'type':'function_call_output',
                      'call_id':item.call_id,
                      'output':json.dumps({'convert_currency':currency_result})
                })
response=client.responses.create(
      model='openai/gpt-oss-20b',
      instructions='respond to the user input using the tool output',
      tools=tools,
      input=messages
)

print(response.output_text)