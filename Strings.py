word = input("Please enter a word: ")

print("Length of word:", len(word))

# Convert to uppercase and lowercase
print("To uppercase:", word.upper())
print("To lowercase:", word.lower())

# Count how many times a letter appears in a word
letter = input("Please enter a letter: ")
print(f" The '{letter}' appears {word.count(letter)} times")