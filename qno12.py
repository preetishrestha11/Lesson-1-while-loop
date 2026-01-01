current_floor = 1

while True:
    try:
        destination = input("Enter destination floor (0 to exit): ")

        if destination == "0":
            print("Goodbye!")
            break

        destination = int(destination)

        if destination > current_floor:
            print("Going up")
        elif destination < current_floor:
            print("Going down")
        else:
            print("You are already on this floor")

        current_floor = destination

    except ValueError:
        print("Please enter a valid number.")
