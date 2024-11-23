# Python calculator

operator = input("Enter an operator (+ - * /) : ")
if operator != "+" and operator != "-" and operator != "*" and operator != "/":
    print("Only these operators are allowed: +, -, *, /")
else:    
    num1 = float(input("Enter the 1st Number"))
    num2 = float(input("Enter the 2nd Number"))

    result = 0

    if operator == '+' :
        print(num1 + num2)
    elif operator == "-" :
        print(num1 - num2)
    elif operator == "*" : 
        print(num1 * num2)
    elif operator == "/" :
        print(num1 / num2)

