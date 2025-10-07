# Write a program to mine a log file and find out whether it contains 'python'

#----Ans
with open("log.txt") as f:
    content = f.read()

if "python" in content:
    print("Yes python is there")
else:
    print("No python is present")

print("End of program")

# Output (example if 'python' is present):
# Yes python is there
# End of program
