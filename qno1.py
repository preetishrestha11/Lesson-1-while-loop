while True:
    age = input("Enter your age (or type 'stop.' to quit): ")

    if age == "stop.":
        break

    age = int(age)

    if age < 18:
        print("You are a minor.")
    elif age <= 60:
        print("You are an adult.")
    else:
        print("You are a senior citizen.")
