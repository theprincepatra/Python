# A spam comment  is defined as a text containing following keywords:
#"make a lot of money","buy now","subscribe this","click this".write a program to detect these spams.


c1 = "make a lot of money"
c2 = "buy now"
c3 = "subscribe this"
c4 = "click this"

msg = input("enter your comment:")

if((c1 is msg) or (c2 is msg) or (c3 is msg) or (c4 is msg)):
    print("This comment is a spam")

else:
    print("This comment is not a spam")

print("End of program")

# Output:
# enter your comment: buy now
# This comment is a spam
# End of program
