while True:
    number1 = int(input("Enter a number: "))
    number2 = int(input("Enter a second number: "))
    operation = input("Enter an action (+, -, *, /): ")

    if operation == "+":
        print(number1 + number2)

    if operation == "-":
        print(number1 - number2)

    if operation == "*":
        print(number1 * number2)

    if operation == "/":
        if number2 != 0:
            print(number1 / number2)
        else:
            print("Error: you can`t divide by zero")

    again = input("Do you want to continue? (y/yes to continue): ").lower()
    if again not in ("y", "yes"):
        break
