import random

number = random.randint(1, 10)
attempts = 0

while True:
    guess = int(input("Guess the number (1-10): "))
    attempts += 1

    if guess < number:
        print("Guess higher")
    elif guess > number:
        print("Guess lower")
    else:
        print(f"Correct! You guessed it in {attempts} attempts.")
        break
