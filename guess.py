import random

secret = random.randint(1, 100)
attempts = 0

while True:
    guess = input("Guess a number (1-100) or 'q' to quit: ")

    if guess == 'q':
        print("You quit. Number was:", secret)
        break

    if not guess.isdigit():
        print("Invalid input")
        continue

    guess = int(guess)
    attempts += 1

    if guess < secret:
        print("Too low")
    elif guess > secret:
        print("Too high")
    else:
        print("Correct! Attempts:", attempts)
        break
