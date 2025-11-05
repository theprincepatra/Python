# Create a class "Programmer" for storing informaton of few programmers working at Microsoft.

# Ans ---
class Programmer:
    company = "Microsoft"
    def __init__(self, name, salary, address):
        self.name = name
        self.salary = salary
        self.address = address

p = Programmer("Prince", 120000, "Balangir")
print(p.name, p.salary, p.address, p.company)

p = Programmer("Pritish", 160000, "Cuttack")
print(p.name, p.salary, p.address, p.company)

p = Programmer("Shivam", 130000, "Puri")
print(p.name, p.salary, p.address, p.company)

print("End of program")


# output:
# Prince 120000 Badambadi Cuttack Balangir
# Pritish 160000 Tulsipur Cuttack Cuttack
# Shivam 130000 Puri Badadanda Puri
# End of program
