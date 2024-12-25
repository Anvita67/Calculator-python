def calculator():
    print("Simple Calculator")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

    try:
        choice = int(input("Choose an option (1-4): "))
        if choice not in [1, 2, 3, 4]:
            print("Invalid choice.")
            return

        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))

        if choice == 1:
            print(f"The result is: {num1 + num2}")
        elif choice == 2:
            print(f"The result is: {num1 - num2}")
        elif choice == 3:
            print(f"The result is: {num1 * num2}")
        elif choice == 4:
            if num2 != 0:
                print(f"The result is: {num1 / num2}")
            else:
                print("Cannot divide by zero.")
    except ValueError:
        print("Invalid input. Please enter numbers.")

if __name__ == "__main__":
    calculator()
