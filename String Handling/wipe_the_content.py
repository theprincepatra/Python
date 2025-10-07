# Write a program to wipe out the content of a file using Python.

#--Ans
with open("imposter.txt", "w") as f:
    f.write("")

print("File content wiped successfully")

# Output:
# File content wiped successfully
