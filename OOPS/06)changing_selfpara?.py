# Can you change the self parameter inside a class to something else (say "Harry")? Try changing self to "slf" or "harry" and see the effects.

from random import randint

class Train:
    def __init__(slf, trainNo):
        slf.trainNo = trainNo

    def book(harry, fro, to):
        print(f"Ticket is booked in train no: {harry.trainNo} from {fro} to {to}")

    def getStatus(self):
        print(f"Train no: {self.trainNo} is running on time")

    def getFare(self, fro, to):
        print(f"Ticket fare in train no: {self.trainNo} from {fro} to {to} is {randint(333, 666)}")


t = Train(7654321)
t.book("Cuttack", "Puri")
t.getStatus()
t.getFare("Cuttack", "Puri")

print("End of program")

# Output:
# Ticket is booked in train no: 7654321 from Cuttack to Puri
# Train no: 7654321 is running on time
# Ticket fare in train no: 7654321 from Cuttack to Puri is <random number between 333 and 666>
# End of program

# Note:
# Yes, you can change 'self' to any name (like 'slf' or 'harry').
# It's just a convention — Python only cares about the first parameter in instance methods referring to the object itself.
