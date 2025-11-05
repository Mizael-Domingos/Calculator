from sympy import symbols, sympify, diff, integrate, limit, lambdify  # type: ignore
import numpy as np
import matplotlib.pyplot as plt


def invalid():
    print("Invalid answer!\n")


def calculate(num1, num2, operator):
    operations = {
        "+": lambda a, b: a + b,
        "-": lambda a, b: a - b,
        "*": lambda a, b: a * b,
        "/": lambda a, b: a / b if b != 0 else None,
    }

    if operator not in operations:
        invalid()
        return None

    if operator == "/" and num2 == 0:
        print("Error: Division by zero")
        return None

    return operations[operator](num1, num2)


def get_number(prompt, default=None):
    if default is None:
        value = input(prompt)
    else:
        value = default

    try:
        return float(value)
    except ValueError:
        invalid()
        return None


def arithmetic_calculator(num_1):
    num1 = get_number("Enter first number: ", num_1)
    if num1 is None:
        return

    operator = input("Enter operation (+,-,*,/): ").strip()
    num2 = get_number("Enter second number: ")
    if num2 is None:
        return

    result = calculate(num1, num2, operator)
    if result is None:
        return

    while True:
        answer = input("Do you want to continue? S/N: ").strip().upper()
        if answer == "S":
            arithmetic_calculator(result)
            break
        elif answer == "N":
            break
        else:
            invalid()

    return result


def calculus_calculator():
    print("Choose operation: 1- Derivative, 2- Integral, 3- Limit")
    calc_type = input()

    print("Enter the variable (e.g., x):")
    variable = input()

    print("Enter the expresion (e.g., x^2 + 3*x + 2):")
    expression = input()

    if calc_type == "1":
        derivative_calc(expression, variable)
    elif calc_type == "2":
        integral_calc(expression, variable)
    elif calc_type == "3":
        limit_calc(expression, variable)
    else:
        invalid()
        calculus_calculator()


def derivative_calc(expression, variable):
    expression = expression.replace("^", "**")
    x = symbols(variable)

    try:
        expr = sympify(expression)
    except Exception as e:
        print("Invalid mathematical expression:", e)
        return

    derivative = diff(expr, x)

    print("Derivative: ", derivative)

    while True:
        answer = input("Do you want to evaluate at a specific point? (y/n) ").lower()
        if answer == "y":
            value = float(input("Enter the value of the variable: "))
            numeric_result = derivative.subs(x, value)
            print("Result at x =", value, "is", numeric_result)
            break
        elif answer == "n":
            break
        else:
            invalid()

    x_vals = np.linspace(-10, 10, 400)

    f = lambdify(x, expr, "numpy")
    df = lambdify(x, derivative, "numpy")

    plt.plot(x_vals, f(x_vals), label="f(x)")

    plt.plot(x_vals, df(x_vals), label="f'(x)", linestyle="--")
    plt.legend()
    plt.title("Function and its Derivative")
    plt.xlabel(variable)
    plt.ylabel("Value")
    plt.grid(True)
    plt.show()

    return derivative, f, df


def integral_calc(expression, variable):
    expression = expression.replace("^", "**")
    x = symbols(variable)

    try:
        expr = sympify(expression)
    except Exception as e:
        print("Invalid mathematical expression:", e)
        return

    while True:
        answer = input("Do you want a definite integral? (y/n) ").lower()
        if answer == "y":
            lower = float(input("Enter lower limit: "))
            upper = float(input("Enter upper limit: "))
            result = integrate(expr, (x, lower, upper))
            print(f"Definite integral from {lower} to {upper}: {result}")

            x_vals = np.linspace(lower - 2, upper + 2, 400)
            f = lambdify(x, expr, "numpy")

            plt.plot(x_vals, f(x_vals), label="f(x)", color="blue")
            plt.fill_between(
                x_vals,
                f(x_vals),
                where=(x_vals >= lower) & (x_vals <= upper),
                color="lightblue",
                alpha=0.4,
                label="Area under curve",
            )
            plt.title(f"Definite Integral from {lower} to {upper}")
            plt.xlabel(variable)
            plt.ylabel("f(x)")
            plt.legend()
            plt.grid(True)
            plt.show()
            return
        elif answer == "n":
            result = integrate(expr, x)
            break
        else:
            invalid()

    print("Integral:", result)

    x_vals = np.linspace(-10, 10, 400)

    f = lambdify(x, expr, "numpy")
    f_integral = lambdify(x, result, "numpy")

    plt.plot(x_vals, f(x_vals), label="f(x)")
    plt.plot(x_vals, f_integral(x_vals), label="∫f(x)dx", linestyle="--")

    plt.fill_between(
        x_vals,
        f(x_vals),
        where=(x_vals > -5) & (x_vals < 5),
        color="lightblue",
        alpha=0.3,
        label="Example area",
    )

    plt.title("Function and Its Integral")
    plt.xlabel(variable)
    plt.ylabel("Value")
    plt.legend()
    plt.grid(True)
    plt.show()

    return integrate, f, f_integral


def limit_calc(expression, variable):
    expression = expression.replace("^", "**")
    x = symbols(variable)
    expr = sympify(expression)

    point = float(input("Enter the point of approach: "))

    while True:
        direction = input(
            "Choose direction: 1- two-sided, 2- from left, 3- from right: "
        )
        if direction == "1":
            result = limit(expr, x, point)
            break
        elif direction == "2":
            result = limit(expr, x, point, dir="-")
            break
        elif direction == "3":
            result = limit(expr, x, point, dir="+")
            break
        else:
            invalid()

    print("Limit result: ", result)
    return result


def converter_calculator():
    while True:
        unit = input("Select a type: 1- Distance, 2- Pressure\n")

        if unit == "1":
            distance_calc()
        elif unit == "2":
            pressure_calc()
        else:
            invalid()


distance_factors = {
    "meters": 1.0,
    "feet": 0.3048,
    "miles": 1609.34,
    "kilometers": 1000,
    "inches": 0.0254,
}


def convert_distance(value, unit1, unit2):
    value_in_meters = value * distance_factors[unit1]

    result = value_in_meters / distance_factors[unit2]
    return result


def distance_calc():
    print("Available units: meters, feet, miles, kilometers, inches")

    unit1 = input("Enter the first unit: ").strip().lower()
    unit2 = input("Enter the unit to convert to: ").strip().lower()
    value = float(input(f"Enter the distance in {unit1}: "))

    if unit1 not in distance_factors or unit2 not in distance_factors:
        invalid()
        return

    result = convert_distance(value, unit1, unit2)
    print(f"{value} {unit1} = {result} {unit2}")


pressure_factors = {
    "pascal": 1,
    "bar": 100000,
    "kilopascal": 1000,
    "atm": 101325,
    "mmhg": 133.3224,
    "psi": 6894.8,
}


def convert_pressure(value, unit1, unit2):
    value_in_pascal = value * pressure_factors[unit1]

    result = value_in_pascal / pressure_factors[unit2]
    return result


def pressure_calc():
    print("Available units: pascal, bar, kilopascal, atm, mmHg, psi")

    unit1 = input("Enter the first unit: ").strip().lower()
    unit2 = input("Enter the unit to convert to: ").strip().lower()
    value = float(input(f"Enter the pressure in {unit1}: "))

    if unit1 not in pressure_factors or unit2 not in pressure_factors:
        invalid()
        return

    result = convert_distance(value, unit1, unit2)
    print(f"{value} {unit1} = {result} {unit2}")
