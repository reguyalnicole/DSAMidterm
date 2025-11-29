import math

while True:
    print("\nSelect an operation to perform:")
    print("1 Add")
    print("2 Subtract")
    print("3 Multiply")
    print("4 Division")
    print("5 Square Root")
    print("6 Exit")

    operation = input("Enter choice (1/2/3/4/5/6): ")

    if operation == "1":
        num1 = input("Enter the first number: ")
        num2 = input("Enter the second number: ")
        result = int(num1) + int(num2)
        print("The sum is:", result)

    elif operation == "2":
        num1 = input("Enter the first number: ")
        num2 = input("Enter the second number: ")
        result = int(num1) - int(num2)
        print("The difference is:", result)

    elif operation == "3":
        num1 = input("Enter the first number: ")
        num2 = input("Enter the second number: ")
        result = int(num1) * int(num2)
        print("The product is:", result)

    elif operation == "4":
        num1 = input("Enter the first number: ")
        num2 = input("Enter the second number: ")
        if int(num2) == 0:
            print("Error: Cannot divide by zero!")
        else:
            result = int(num1) / int(num2)
            print("The quotient is:", result)

    elif operation == "5":
        num = input("Enter the number: ")
        if float(num) < 0:
            print("Error: Cannot take square root of a negative number!")
        else:
            result = math.sqrt(float(num))
            print("The square root is:", result)

    elif operation == "6":
        break   # Exit without printing anything

    else:
        print("Invalid input!")
