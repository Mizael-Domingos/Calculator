from sympy import symbols, sympify, diff, integrate, limit # type: ignore


def arithimetic_calculator(num_1):
    if num_1 == None:
        print("Enter first number:")
        num1 = input()
    else:
        num1 = num_1

    print("Enter operation (+,-,*,/)")
    operator = input()
    print("Enter second number:")
    num2 = input()

    if operator == "+":
        result = float(num1) + float(num2)
    elif operator == '-':
        result = float(num1) - float(num2)
    elif operator == '*':
        result = float(num1) * float(num2)
    elif operator == '/':
        if num2 == "0":
            print("Error: Division by zero")
            return
        else:
            result = float(num1) / float(num2)
    else:
        print("Invalid operator")
    
    print("Result: ", result)
    

    while True:
        answer = input('Do you want to continue? S/N: ')
        if answer.upper() == 'S':
            arithimetic_calculator(result)
            break
        elif answer.upper() == 'N':
            break
        else:
            print("Invalid answer")

    

def calculus_calculator():
    print("Choose operation: 1- Derivative, 2- Integral, 3- Limit")
    calc_type = input()

    print("Enter the variable (e.g., x):")
    variable = input()

    print("Enter the expresion (e.g., x^2 + 3*x + 2):")
    expression= input()

    if calc_type == "1":
        derivative_calc(expression, variable)
    elif calc_type == "2":
        integral_calc(expression, variable)
    elif calc_type == "3":
        limit_calc(expression, variable)
    else:
        print("Invalid option")
        calculus_calculator()


def convert(expression, variable):
    expression = sympify(expression)
    variable = symbols(variable)
    
    return expression, variable

def derivative_calc(expression, variable):
    expression, variable = convert(expression, variable)

    derivative = diff(expression,variable)

    print("Derivative: ", derivative)

    answer = input("Do you want to evaluate at a specific point? (y/n) ").lower()
    if answer == "y":
        value = float(input("Enter the value of the variable: "))
        numeric_result = derivative.subs(variable, value)
        print("Result at x =", value, "is", numeric_result)

    

def integral_calc(expression, variable):
    expression, variable = convert(expression, variable)

    answer = input("Do you want a definite integral? (y/n) ").lower()
    if answer == "y":
        lower = float(input("Enter lower limit: "))
        upper = float(input("Enter upper limit: "))
        result = integrate(expression, (variable, lower, upper))
    else:
        result = integrate(expression, variable)
    
    print("Integral:", result)


def limit_calc(expression, variable):
    expression, variable = convert(expression, variable)

    point = input("Enter the point of approach: ")
    direction = input("Choose direction: 1- two-sided, 2- from left, 3- from right: ")

    while True:
        direction = input("Choose direction: 1- two-sided, 2- from left, 3- from right: ")
        if direction == "1":
            result = limit(expression, variable, point)
            break
        elif direction == "2":
            result = limit(expression, variable, point, dir='-')
            break
        elif direction == "3":
            result = limit(expression, variable, point, dir='+')
            break
        else:
            print("Invalid direction")

    print("Limit result: ", result)