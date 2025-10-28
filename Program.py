from calculator import arithimetic_calculator, calculus_calculator # type: ignore

while True:
    print("Choose mode: 1- Arithmetic, 2- Calculus")
    mode = input()

    if mode == "1":
        num1 = None
        arithimetic_calculator(num1)
        break
    elif mode == "2":
        calculus_calculator()
        break
    else:
        print("Invalid mode selected")
