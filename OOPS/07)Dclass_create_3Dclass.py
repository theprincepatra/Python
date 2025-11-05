# Create a class (2-D vector) and use it to create another class representing 3D vector.

class TwoDVector:
    def __init__(self, i, j):
        self.i = i
        self.j = j

    def show(self):
        print(f"The Vector is {self.i}i + {self.j}j")


class ThreeDVector(TwoDVector):
    def __init__(self, i, j, k):
        super().__init__(i, j)
        self.k = k  # fixed: removed '+=' typo

    def show(self):
        print(f"The Vector is {self.i}i + {self.j}j + {self.k}k")


x = TwoDVector(3, 4)
x.show()

y = ThreeDVector(3, 4, 6)
y.show()

print("End of program")

# Output:
# The Vector is 3i + 4j
# The Vector is 3i + 4j + 6k
# End of program
