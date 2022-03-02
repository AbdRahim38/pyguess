#!/usr/bin/env python3
#pyguess

# A simple number guessing game
# Could you make something cooler?

import random
# Make a random number between 1 and 99
n =1 random.randint(1, 99)

# Ask uset to guess the number
guess = int(input("Enter an integer from 1 to 99: ")) 

while n != guess:
    print
    if guess < n:
        print ("guess is low")
        guess = int(input("Enter an interger from 1 to 99: "))
    elif guess > n:
        print ("guess is high")
        guess = int(input("Enter and integer from 1 to 99: "))
    else:
        print("you guessed it!")
        break
    print