# Guess the number
# Python 3.0+

# Maximum number = user input
# Shows the number of guesses

import random

print("Welcome to the guess the number game")

# Set the maximum number
max_num = int(input("Enter the maximum number: "))

# Generate the random number within the interval
n = random.randint(1, max_num)

# Guess the number
guess = int(input("Enter an integer from 1 to " + str(max_num) + ": "))
guess_used = 0


if guess < n: # Too low
    print("Guess is too low. Try again")
    guess = int(input("Enter an integer from 1 to " + str(max_num) + ": "))
    guess_used += 1
elif guess > n: # Too high
    print("Guess is too high. Try again")
    guess = int(input("Enter an integer from 1 to " + str(max_num) + ": "))
    guess_used += 1  


print("You guessed it in " + str(guess_used) + " guesses!")
print("Thank you for playing")