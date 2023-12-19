# Calculator ;

number1 = float(input("Enter the first number : "))
number2 = float(input("Enter the second number : "))
operator = input("Enter the operator (+, -, *, /) : ")

if operator == "+" :
    result = number1 + number2
elif operator == "-" :
    result = number1 - number2
elif operator == "*" :
    result = number1 * number2
elif operator == "/" :
    result = number1 / number2
else:
    print("Invalid operator !")

print("Result :", result)

try:
    number1 = float(input("Enter the first number : "))
    number2 = float(input("Enter the second number : "))
    operator = input("Enter the operator (+, -, *, /) : ")

    if operator == "+" :
        result = number1 + number2
    elif operator == "-" :
        result = number1 - number2
    elif operator == "*" :
        result = number1 * number2
    elif operator == "/" :
        result = number1 / number2
    else:
        print("Invalid operator !")

    print("Result :", result)

except ValueError:
    print("Invalid number input !")
