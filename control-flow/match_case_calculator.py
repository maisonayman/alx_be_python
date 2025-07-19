num1 = int(input("Enter the first number:"))

num2 = int(input("Enter the second number:"))

operation = input("Choose the operation (+, -, *, /):")

match operation:
    case "+":
        print(f"Result: {num1 + num2}")
    case "-":
        print(f"Result: {num1 - num2}")
    case "*":
        print(f"Result: {num1 * num2}")
    case "/":
        if num2 == 0:
            print("Error: Cannot divide by zero.")
        else:
            print(f"Result: {num1 / num2}")
    case _:
        print("Invalid operation.")