from api_connection import get_response_dual


base_system_prompt = "Act as a learning advisor who receives queries from users mentioning their background, experience, and goals, and accordingly provides a response that recommends a tailored learning path of textbooks, including both beginner-level and more advanced options."

# Define behavior guidelines
behavior_guidelines = "ask a user about their background, experience, and goals"

# Define response guidelines
response_guidelines = "recommend no more than three textbooks to the user"

system_prompt = base_system_prompt + behavior_guidelines + response_guidelines
user_prompt = "Hey, I'm looking for courses on Python and data visualization. What do you recommend?"
response = get_response_dual(system_prompt, user_prompt)
print(response)