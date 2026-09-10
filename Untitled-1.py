print("===CALCULATOR===")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
choice = int(input("Enter your choice: "))
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
if choice == 1:
    print("the sum of two numbers is: ", a + b)
elif choice == 2:
    print("the difference of two numbers is: ", a - b)
elif choice == 3:
    print("the product of two numbers is: ", a * b)
elif choice == 4:
    if b != 0:
        print("the division of two numbers is: ", a / b)
    else:
        print("division by zero is not allowed")
else:
    print("Invalid choice")