a = float (input("enter first number: "))
b = float (input("enter second number: "))

print("the sum of two numbers is: ", a + b)
print("the difference of two numbers is: ", a - b)
print("the product of two numbers is: ", a * b)
if b != 0:
    print("the division of two numbers is: ", a / b)
    print("the modulus of two numbers is: ", a % b)
    print("the floor division of two numbers is: ", a // b) 
else:
    print("division ,modulus and floor division are not possible as second number is zero")
    print("the power of two numbers is: ", a ** b)