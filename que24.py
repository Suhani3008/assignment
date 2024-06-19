#Write a program that acts as a simple calculator. It should take two numbers and an operator (+, -, *, /) as input and print the result

num1 = float(input("Enter the first number : "))

operator = input("Enter the operator (+,-,*,/) : ")

num2 = float(input("Enter the second number : "))

if operator == '+':
    result = num1+num2
elif operator == '-':
    result = num1-num2
elif operator == '*':
    result = num1*num2
elif operator == '/':

    if num2 != 0:
      result = num1/num2
    else:
        print("ERROR : Divison by zero.")
        result = None
else:
    print("INVALID OPERATOR !!!")

if result is not None:
    print(f"Result: {num1} {operator} {num2} = {result}")