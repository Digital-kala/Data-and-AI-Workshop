def calculator():
    # Get the first number from the user
    num1 = float(input("Enter first number: "))
    
    # Get the second number from the user
    num2 = float(input("Enter second number: "))
    
    # Get the operation from the user
    operation = input("Enter operation (+, -, *, /): ")
    
    # Perform the operation and print the result
    if operation == '+':
        print(num1 + num2)  # Add
    elif operation == '-':
        print(num1 - num2)  # Subtract
    elif operation == '*':
        print(num1 * num2)  # Multiply
    elif operation == '/':
        print(num1 / num2)  # Divide
    else:
        # Print an error message if the operation is invalid
        print("Invalid operation")

# Run the calculator
calculator()