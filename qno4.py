while True:
    password = input("Guess the password: ")

    if password == "open sesame":
        print("Access granted!")
        break
    else:
        print("Wrong password, try again.")
