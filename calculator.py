def calculator():

    # Define functions for the four basic operations
    def add(x, y):
        return x + y

    def subtract(x, y):
        return x - y

    def multiply(x, y):
        return x * y

    def divide(x, y):
        if y != 0:
            return x / y
        else:
            return "Error! Division by zero."

    # Display menu
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

    # Get input from the user
    choice = input("Enter choice(1/2/3/4): ")

    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if choice == '1':
        print(f"{num1} + {num2} = {add(num1, num2)}")

    elif choice == '2':
        print(f"{num1} - {num2} = {subtract(num1, num2)}")

    elif choice == '3':
        print(f"{num1} * {num2} = {multiply(num1, num2)}")

    elif choice == '4':
        print(f"{num1} / {num2} = {divide(num1, num2)}")

    else:
        print("Invalid input")



while True:
    calculator()
    
     # Ask if the user wants to play again
    ans=input("Do you want to play again?? press enter to Quit the game or any key to replay")
    if ans == '':
            break

# After coming out of the while loop, print thanks for playing
print("Thanks for playing!")
