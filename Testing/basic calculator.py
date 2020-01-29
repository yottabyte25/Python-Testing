num1 = float(input("Enter your first number: "))
op = input("Enter the operation you would like to execute: ")
num2 = float(input("Enter your second number: "))
if op == "+":
    print(num1 + num2)
elif op == "-":
    print(num1 - num2)
elif op == "*":
    print(num1 * num2)
elif op == "/":
        print(num1 / num2)
else:
    print("Invalid Operator. (Note the operators must be either +,-,*,// )")