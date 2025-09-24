# Print the following star pattern .
'''
* * *
*   *
* * *
'''


n = int(input("enter a number:"))
for i in range(1, n+1):
    if i == 1 or i == n:
        print("* " * n)
    else:
        print("*" + " " * (2*n - 3) + "*")

# Output:
# enter a number:3
# * * *
# *   *
# * * *
