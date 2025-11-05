# Write a class Train which has methods to book a ticket, get status (no of seats), and get fare information of trains running under Indian Railways.

from random import randint

class Train:
    def __init__(self, trainNo):
        self.trainNo = trainNo

    def book(self, fro, to):
        print(f"Ticket is booked in train no: {self.trainNo} from {fro} to {to}")

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
