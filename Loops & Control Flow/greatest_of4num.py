# Write a program to find the greatest of four numbers entered by the user.

# Ans ---
# signing in 
a1 = int(input("enter a number 1"))
a2 = int(input("enter a number 2"))
a3 = int(input("enter a number 3"))
a4 = int(input("enter a number 4"))

if(a1>a2 and a1>a3 and a1>a4):
    print("Greatest number is a1:",a1)

elif(a2>a1 and a2>a3 and a2>a4):
    print("Greatest number is a2:",a2)

elif(a3>a1 and a3>a2 and a3>a4):
    print("Greatest number is a3:",a3)

else:
    print("Greatest number is a4",a4)

print("End of the program")

#Output:
#enter a number 1: 12
#enter a number 2: 45
#enter a number 3: 33
#enter a number 4: 45
#Greatest number is a4 45
#End of the program
