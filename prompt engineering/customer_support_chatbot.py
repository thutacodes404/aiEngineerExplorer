from api_connection import get_response_dual

# Define the purpose of the chatbot
chatbot_purpose = "handles customer support, specializes in electronics, and is there to assist with inquiries, order tracking, and troubleshooting"

# Define audience guidelines
audience_guidelines = "tech-savvy individuals interested in purchasing electronic gadgets"

# Define tone guidelines
tone_guidelines = "use a professional and user-friendly tone while interacting with customers."

system_prompt = chatbot_purpose + audience_guidelines + tone_guidelines
response = get_response_dual(system_prompt, "My new headphones aren't connecting to my device")
print(response)