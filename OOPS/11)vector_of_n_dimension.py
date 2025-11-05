# Write a class Vector representing a vector of n dimensions. Overload the + and * operators which calculate the sum and the dot (.) product of them.

class Vector:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __add__(self, other):
        result = Vector(self.x + other.x, self.y + other.y, self.z + other.z)
        return result

    def __mul__(self, other):
        result = self.x * other.x + self.y * other.y + self.z * other.z
        return result

    def __str__(self):
        return f"Vector({self.x}, {self.y}, {self.z})"


# Test the implementation
v1 = Vector(1, 2, 3)
v2 = Vector(4, 5, 6)
v3 = Vector(7, 8, 9)

print(v1 + v2)
print(v1 * v2)

print(v1 + v3)
print(v1 * v3)

print("End of program")

# Output:
# Vector(5, 7, 9)
# 32
# Vector(8, 10, 12)
# 50
# End of program
