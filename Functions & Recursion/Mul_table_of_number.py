# Write a program to print multiplication table of a given number using for loop.

n = int(input("enter a number"))

for i in range (1,11):
    print(f"{n} x {i} = {n*i}")

print("end of program")

#output:
#enter a number5
#5 x 1 = 5
#5 x 2 = 10
#5 x 3 = 15
#5 x 4 = 20
#5 x 5 = 25
#5 x 6 = 30
#5 x 7 = 35
#5 x 8 = 40
#5 x 9 = 45
#5 x 10 = 50
#end of program
