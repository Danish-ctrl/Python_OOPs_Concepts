"""
Create a program that takes a sentence as input and
counts the number of words in it
"""
sentence = "My name is Danish"

# Split the sentence into words using whitespace as the delimiter
words = sentence.split()

# Count the number of words
word_count = len(words)

print("Words count:", word_count)
