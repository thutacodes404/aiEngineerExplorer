def word_counting_file(filename):
    try:
        with open(filename, 'r') as file:
            contents = file.readlines()
        word_count = 0
        for line in contents:
            words = line.split()
            word_count += len(words)
        print(f"The file '{filename}' contains {word_count} words.")    
    except FileNotFoundError:
        print(f"The file '{filename}' was not found.")

# Example usage:
filename = 'example.txt'  # Replace with your file name
word_counting_file(filename)