import re

text = "The rain in Spain stays mainly in the plain. Contact us at 123-456-7890 or visit our website at www.example.com."

digits = re.findall(r'\d+', text)
print(digits)

modified_text = re.sub(r'\d+', 'XXX', text)
print(modified_text)