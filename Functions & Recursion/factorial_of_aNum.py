# Write a program to calculate the factorial of a given number using for loop .


n = int(input("enter the number:"))
product = 1 
for i in range (1,n+1):
    product = product * i

print(f"The factorial of {n} is {product}")

print("end of program")

# Output:
# enter the number:5
# The factorial of 5 is 120
# end of program
