# Write a program to find the sum of first n natural numbers using while loop .


n = int(input("enter the number:"))
i = 1 
sum = 0
while(i<=n):
    sum += i
    i = i + 1

print(sum)
print("end of program")

# Output:
# enter the number:5
# 15
# end of program
