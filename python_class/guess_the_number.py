#!/usr/bin/python3

import random
secretNumber = random.randint(1, 20)
print("I'm thinking of a number between 1 and 20")

#Ask the player to guess up to 6 times
for guesses in range (1, 7):
    print("Take a guess.")
    guess = int(input())

    if guess < secretNumber:
        print("\nYour guess is too low.\n")
    elif guess > secretNumber:
        print("\nYour guess is too high.\n")
    else:
        break #Correct guess condition

if guess == secretNumber:
    print("Good job! You guessed my number in " + str(guesses) + " guesses!")
else:
    print("Nope. The number I was thinking of was " + str(secretNumber))
