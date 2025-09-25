# Write a program to find whether a given username contains less than 10 characters or not.


name = input("enter name:")

if(len(name) < 10):
    print("name has less than 10 characters",name)

else:
    ("invalid name",name)

print("END OF PROGRAM")

# Output:
# enter name: Prince
# name has less than 10 characters Prince
# END OF PROGRAM
