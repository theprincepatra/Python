# Write a class "Calculator" capable of finding square, cube and square root of a number.

class Calculator:
    def __init__(self, n):
        self.n = n

    def square(self):
        print(f"The square is {self.n * self.n}")

    def cube(self):
        print(f"The cube is {self.n * self.n * self.n}")

    def squareroot(self):
        print(f"The square root is {self.n ** 0.5}")


a = Calculator(9)
a.square()
a.cube()
a.squareroot()

print("End of program")

# Output:
# The square is 81
# The cube is 729
# The square root is 3
# End of program
