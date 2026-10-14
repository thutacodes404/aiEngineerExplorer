# few shot prompting with a chat model

response= client.chat.completions.create(
    model='gpt-4o-mini',
    messages=[
        {'role':'user',
         'content':'today the weather is fantastic'},
         {'role':'assistant',
          'content':'positive'},
          {'role':'user',
           'content':"i don't like your attitude "},
           {'role':'assistant',
            'content':'negative'},
            {'role':'user',
             'content':'that shot selection was awful'}
    ],
    temperature=0
)

print(response.choices[0].message.content)