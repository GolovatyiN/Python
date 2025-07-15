number = int(input("Enter a 5-digit number: "))

digit1 = number // 10000
digit2 = (number % 10000) // 1000
digit3 = (number % 1000) // 100
digit4 = (number % 100) // 10
digit5 = number % 10

print(digit5 * 10000 + digit4 * 1000 + digit3 * 100 + digit2 * 10 + digit1)