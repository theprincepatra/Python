# Write a Python program to rename a file to "renamed_by_python.txt".

#--Ans
with open("old.txt") as f:
    content = f.read()

with open("renamed_by_python.txt", "w") as f:
    f.write(content)

print("File has been renamed and content copied successfully")

# Output:
# File has been renamed and content copied successfully
