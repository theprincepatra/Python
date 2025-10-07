# A file contains the word "Donkey" multiple times. You need to write a program that replaces this word with "Parimal" by updating the same file.

# Ans --- 
word = "Donkey"

with open("Donkey.txt", "r") as f:
    content = f.read()

contentNew = content.replace(word, "Parimal")

with open("Donkey.txt", "w") as f:
    f.write(contentNew)

# Output:
# All occurrences of "Donkey" in Donkey.txt are replaced with "Parimal"
