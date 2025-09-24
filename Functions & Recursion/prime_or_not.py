# Write a program to find whether a given number is prime or not.


n = int(input("enter a number:"))

for i in range(2,n):
    if(n%i) == 0:
        print("Number is not prime")
        break
else:
    print("Number is prime")

print("END OF PROGRAM")

# Output:
# enter a number:7
# Number is prime
# END OF PROGRAM
