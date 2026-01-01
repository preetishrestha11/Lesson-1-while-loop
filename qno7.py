attempts = 0

while attempts < 3:
    username = input("Username: ")
    password = input("Password: ")

    if username == "admin" and password == "1234":
        print("Login successful")
        break
    else:
        print("Invalid credentials, try again.")
        attempts += 1

if attempts == 3:
    print("Too many failed attempts.")
