#Task 1: Create functions for each arithmetic operation.

operation = input("1.  Add 2.  Subtract 3.  Multiply 4.  Divide ")


if operation == "1":
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    print(f"The sum is  {num1 + num2}")
elif operation == "2":
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    print(f"The difference is  {num1 - num2}")
elif operation == "3":
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    print(f"The mutiplication is  {num1 * num2}")
elif operation == "4":
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    print(f"The product is  {num1 / num2}")
else:
    print("Invalid Entry")
