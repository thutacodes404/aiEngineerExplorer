from api_connection import get_response_dual

service_description = """
MyPersonalDelivery is a personal delivery service that provides fast, reliable, and convenient delivery for individuals and businesses. 
Customers can schedule deliveries, track their orders in real time, and choose flexible delivery options. 
The service offers same-day delivery in selected areas, secure handling of packages, and customer support for delivery-related questions.
"""

# Define the system prompt
system_prompt = f""" you are a customer service chatbot for a delivery service that responds in a gentle way and point to a service description that I provided```{service_description}``` """

user_prompt = "What benefits does MyPersonalDelivery offer?"

# Get the response to the user prompt
response = get_response_dual(system_prompt,user_prompt)

print(response)