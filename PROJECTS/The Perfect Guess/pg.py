from random import randint
n = randint(1, 100)

a = -1
guess = 0
print("NUMBER HAS BEEN CHOOSEN BY THE USER, now its your trun to guess it......")
while(a != n):
    guess += 1
    a = int(input("Guess the number: "))
    if(a > n):
        print("Lower number please!!")
    else:
        print("Higher number please!!")

print(f"You have guessed the number {n} in {guess} attempt.")

# NUMBER HAS BEEN CHOOSEN BY THE USER, now its your trun to guess it......
# Guess the number: 88
# Lower number please!!
# Guess the number: 50
# Lower number please!!
# Guess the number: 20
# Higher number please!!
# Guess the number: 35
# Higher number please!!
# Guess the number: 45
# Lower number please!!
# Guess the number: 40
# Lower number please!!
# Guess the number: 37
# Lower number please!!
# Guess the number: 36
# Higher number please!!
# You have guessed the number 36 in 8 attempt.
