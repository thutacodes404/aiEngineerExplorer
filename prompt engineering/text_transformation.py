from api_connection import get_response
sample_email = """
Hey John,

We noticed that you haven't used our service in a while. If you're having
any problems, please let us know. We also have some new features that you
might find useful.

Thanks,
The Support Team
"""
# Craft a prompt to change the email's tone
prompt = f"""transform the text in the delimiter ```{sample_email}``` by changing its tone to be professional, positive, and user-centric."""

response = get_response(prompt)

print("Before transformation: \n", sample_email)
print("After transformation: \n", response)