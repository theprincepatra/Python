# Write a program to find out the line number where python is present from previous quesiton "find_python.py".

#----Ans
with open("sexy.txt") as f:
    lines = f.readlines()

lineno = 1
for line in lines:
    if "python" in line:
        print(f"Yes python is present. Line no: {lineno}")
        break
    lineno += 1
else:
    print("No python is present")

print("End of program")

# Output (example if 'python' is in line 3):
# Yes python is present. Line no: 3
# End of program
