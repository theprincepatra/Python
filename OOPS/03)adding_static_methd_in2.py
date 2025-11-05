# Add a static method in problem 2 to greet the user with hello.

class Calculator:
    def __init__(self, n):
        self.n = n

    def square(self):
        print(f"The square is {self.n * self.n}")

    def cube(self):
        print(f"The cube is {self.n * self.n * self.n}")

    def squareroot(self):
        print(f"The square root is {self.n ** 0.5}")

    @staticmethod
    def hello():
        print("Hello")


a = Calculator(6)
a.square()
a.cube()
a.squareroot()
a.hello()

print("End of program")

# Output:
# The square is 36
# The cube is 216
# The square root is 2.449489742783178
# Hello
# End of program
