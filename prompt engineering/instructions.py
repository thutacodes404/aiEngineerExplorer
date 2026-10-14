client = OpenAI(api_key="<OPENAI_API_TOKEN>")

# Create the instructions
instructions = "You will be provided with a text delimited by triple backticks. Infer its language and the number of sentences it contains." \
" Then, if the text has more than one sentence, generate a suitable title for it." \
" Otherwise, if the text contains only one sentence, write 'N/A' for the title."

# Create the output format
output_format = """The output should follow this format:
          - Text: <the given text>
          - Language: <the text language>
          - Title: <the generated title, or N/A>'."""

prompt = instructions + output_format + f"```{text}```"
response = get_response(prompt)
print(response)