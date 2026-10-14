with open("example.txt", "w") as file:
    file.write("Hello, World!\n")
    file.writelines(["This is an example of file handling in Python.\n"],["File handling allows you to read and write files.\n"])


with open("example.txt", "r") as file:
    content = file.read()
    print(content)