secret = "python"

while True:
    guess = input("Guess the secret word (or 'quit' to exit): ").lower()

    if guess == "quit":
        break
    elif guess == secret:
        print("Congratulations, you guessed the word!")
        break
    else:
        print("Incorrect, try again")
