import random

while True:
    num1 = random.randint(1, 30)
    num2 = random.randint(1, 30)

    answer = input(f"What is {num1} x {num2}? (type 'exit' to quit): ")

    if answer.lower() == "exit":
        break

    if int(answer) == num1 * num2:
        print("Correct!")
    else:
        print("Incorrect, try again.")
