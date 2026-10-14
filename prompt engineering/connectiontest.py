client=OpenAI(api_key='')

conversation_message=[
    {"role":'system',
     'content':'you are a helpful event management assistant'},
     {'role':'user',
      'content':'what are some good vonversation starters at networking event'},
      {'role':'assistant',
       'content':''}
]

response=client.chat.completions.create(
    model='gpt-4o-mini',
    messages=conversation_message
)

print(response.choices[0].message.content)