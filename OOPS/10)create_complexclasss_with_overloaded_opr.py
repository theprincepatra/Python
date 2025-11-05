# Write a class ‘Complex’ to represent complex numbers, along with overloaded operators ‘+’ and ‘*’ which adds and multiplies them.

class Complex:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def __add__(self, other):
        return Complex(self.real + other.real, self.imag + other.imag)

    def __mul__(self, other):
        real_part = self.real * other.real - self.imag * other.imag
        imag_part = self.real * other.imag + self.imag * other.real
        return Complex(real_part, imag_part)

    def __str__(self):
        return f"{self.real} + {self.imag}i"


# Example usage
c1 = Complex(2, 3)
c2 = Complex(4, 5)

sum_result = c1 + c2
mul_result = c1 * c2

print("Sum:", sum_result)
print("Product:", mul_result)

print("End of program")

# Output:
# Sum: 6 + 8i
# Product: -7 + 22i
# End of program
