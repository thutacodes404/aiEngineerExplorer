first="hello"
second='world'

print(first+" "+second)

# slicing

text="hello python world"
print(text[1:5])

name="kira"
age=25

print(f"my name is {name} and i am {age} years old")

# split method

sent='Python, is fun, for real'
sen_split=sent.split(",")
print(sen_split)

new_sent="|".join(sen_split)
print(new_sent)

update_text=sent.replace("Python","Java")

print(update_text)

messy="     hello    world"
print(messy.strip())