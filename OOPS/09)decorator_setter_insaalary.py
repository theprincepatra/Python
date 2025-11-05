# Create a class 'Employee' and add salary and increment properties to it.
# Write a method salaryAfterIncrement with a @property decorator and a setter which changes the value of increment based on the salary.

class Employee:
    salary = 643
    increment = 68

    @property
    def salaryAfterIncrement(self):
        return self.salary + self.salary * (self.increment / 100)

    @salaryAfterIncrement.setter
    def salaryAfterIncrement(self, salary):
        self.increment = ((salary / self.salary) - 1) * 100


e = Employee()
print(e.salaryAfterIncrement)
e.salaryAfterIncrement = 1080.24
print(e.increment)

print("End of program")

# Output:
# 1080.24
# 68.00000000000001
# End of program
