print("Basic Calculator")

num1 = float(input("First number: "))
num2 = float(input("Second number: "))

operation = input("Enter desired operation (+, -, *, /, %, //, **): ")

if operation == "+":
    print(num1 + num2)
elif operation == "-":
    print(num1 - num2)
elif operation == "*":
    print(num1 * num2)
elif operation == "/":
    print(num1/num2)
elif operation == "//":
    print(num1//num2)
elif operator == "%":
    print(num1 % num2)
elif operator == "**":
    print(num1 ** num2)
else:
    print("Invalid operator")