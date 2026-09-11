print("A Basic Calculator")

print("Enter two numbers to perform an Operation:")
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
print("Select Operator like +, -, *, /")
operator = input("Enter the operator type:")

if operator == '+':
    result = num1 + num2
elif operator == '-':
    result = num1 - num2
elif operator == '*':
    result = num1 * num2
elif operator == '/':
    if num2 != 0:
        result = num1 / num2
    else:
        result = "Error! Division by zero."
else:
    result = "Invalid operator!"

print("The result of", num1, operator, num2, "is:", result)