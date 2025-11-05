import random
word = input("What is your choice? ")
me = word.lower()
word2 = random.choice(["Snake", "Water", "Gun"])
person = word2.lower()

print("--------------------")
print(f"Your choice is: {word} \nPerson choice is: {word2}")

if(me == person):
    print("Its a draw!!")
elif(me == "snake" and person == "water"):
    print("YOU ARE THE WINNER!!")
elif(me == "snake" and person == "gun"):
    print("HE IS THE WINNER!!")
elif(me == "water" and person == "snake"):
    print("HE IS THE WINNER!!")
elif(me == "water" and person == "gun"):
    print("YOU ARE THE WINNER!!")
elif(me == "gun" and person == "water"):
    print("HE IS THE WINNER!!")
elif(me == "gun" and person == "snake"):
    print("YOU ARE THE WINNER!!")
else:
    print("THERE IS AN ERROR!")

# What is your choice? snake
# --------------------
# Your choice is: snake 
# Person choice is: Water
# YOU ARE THE WINNER!!
