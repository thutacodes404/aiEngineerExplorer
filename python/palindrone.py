def is_palindrone(s):
    s = ''.join(c.lower() for c in s if c.isalnum())
    return s == s[::-1]
if __name__ == "__main__":
    test_cases = [

        "A man, a plan, a canal, Panama",
        "No 'x' in Nixon",
        "Hello, World!",
        "Was it a car or a cat I saw?",
        "Madam In Eden, I'm Adam",
    ]
    for test in test_cases:        
        result = is_palindrone(test)
        print(f"'{test}' is a palindrome: {result}")            
