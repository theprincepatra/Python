# Write a program to find out whether a given post is talking about "Prince"or not.


post = input("enter the post:")

if("Prince".lower() in post.lower()):
    print("This post is talking about prince")
else:
    print("No Prince")
print("END OF PROGRAM")

# Output:
# enter the post: Today I met Prince at the park
# This post is talking about Prince
# END OF PROGRAM
