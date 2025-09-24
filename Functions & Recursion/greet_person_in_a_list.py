# Write a program to greet all the person names stored in a list 'l' and which starts with p .
#l = ["Harry , "spy" , "prince" , "TPP"]


l = ["Harry" , "spy" , "prince" , "TPP"]

for name in l:
    if(name.startswith("p")):
        print(f"Hello{name}")

print("end of program")

# Output:
# Helloprince
# end of program
