

product_description='The SoundCore Q11i is a wireless over-ear headphone designed for everyday listening.It features Bluetooth connectivity, powerful bass, long battery life, and a comfortable over-ear design. It can be used for music, movies, gaming, online classes, and phone calls.'

# Craft a prompt to expand the product's description
prompt = f"""expand the delimited text ```{product_description}``` and writes a one paragraph comprehensive overview capturing the key information of the product: unique features, benefits, and potential applications.
"""

response = get_response(prompt)

print("Original description: \n", product_description)
print("Expanded description: \n", response)