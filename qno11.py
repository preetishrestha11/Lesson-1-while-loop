count = 0

while count < 3:
    word = input("Enter a phrase: ").lower()

    if word == "good luck":
        count += 1
        if count < 3:
            print(f"You typed the same word {count} times.")
        else:
            print("You typed good luck three times.")
