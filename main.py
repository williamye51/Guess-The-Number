import random

# Initialize variables
attempts = 0
maxAttempts = 3
guess = -1
minVal = 1
maxVal = 10

# Generate random integer
secretNumber = random.randint(minVal, maxVal)
print("Pick a number between %d and %d inclusive" % (minVal, maxVal))
print("You have %d attempts" % maxAttempts)

while attempts < maxAttempts:
    # Increment attempts
    attempts += 1

    # User input as guess
    guess = int(input("Guess: "))

    # If guess is correct
    if guess == secretNumber:
        break
    
    # If guess is too low
    elif guess < secretNumber:
        print("Guess is too low.")

    # If guess it too high
    elif guess > secretNumber:
        print("Guess is too high.")

# If user wins
if guess == secretNumber:
    print("Congratulations, You Win!")

# If user loses   
else:
    print("The number is %d." % secretNumber)
    print("Game Over!")