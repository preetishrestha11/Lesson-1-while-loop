while True:
    user_input = input("Enter a number (or 'exit' to quit): ")

    if user_input.lower() == "exit":
        break

    num = int(user_input)

    if num > 1:
        is_prime = True
        for i in range(2, num):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            print("The number is prime.")
        else:
            print("The number is not prime.")
    else:
        print("The number is not prime.")
