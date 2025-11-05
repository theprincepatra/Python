# Create a class with a class attribute 'a'; create an object from it and set 'a' directly using object a = 0. Does this change the class attribute?

class Demo:
    a = 5

o = Demo()
print(o.a) 

o.a = 0
print(o.a)
print(Demo.a)
print("End of program")

# No, this does not change the class attribute.

# Output:
# 5
# 0
# 5
# End of program
