from api_connection import get_response_dual

base_system_prompt = """You are a helpful customer support assistant. 
Answer the user's questions clearly, politely, and concisely. 
Provide useful troubleshooting steps when appropriate and ask for 
necessary information when you need it to resolve the user's issue."""

# Define the order number condition
order_number_condition = "check if submitted a query about an order without specifying an order number"

# Define the technical issue condition
technical_issue_condition = "start the response with I'm sorry to hear about your issue with ... if the user is reporting a technical issue."

# Create the refined system prompt
refined_system_prompt = base_system_prompt+order_number_condition+technical_issue_condition

response_1 = get_response_dual(refined_system_prompt, "My laptop screen is flickering. What should I do?")
response_2 = get_response_dual(refined_system_prompt, "Can you help me track my recent order?")

print("Response 1: ", response_1)
print("Response 2: ", response_2)