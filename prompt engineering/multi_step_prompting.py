client=OpenAI(api_key='')

code='''
    def calculate_area(len,width):
        area=len*width
        return area
'''

prompt=f"""
    check the delimited ```{code} ``` list the steps to analyze a function for correct syntax , 2 inputs and 1 output
"""

response= get_response(prompt)
print(response)