# class DiscriminantError(Exception):
#     pass
#
# a = float(input("Enter a: "))
# b = float(input("Enter b: "))
# c = float(input("Enter c: "))
#
# D = b**2 - 4*a*c
#
# try:
#     if D < 0:
#         raise DiscriminantError("Дискриминант отрицательный")
#
#     sqrt_D = D**0.5
#     x1 = (-b + sqrt_D) / (2*a)
#     print("x1 =", x1)
#
# except DiscriminantError as e:
#     print("Ошибка:", str(e))
#
#
#

formula = input("Enter your request, for example 1 + 1 (use space): ")

symbols = formula.split()

try:
    if len(symbols) > 3:
        raise ValueError("Try again. Use exactly 2 numbers and one action.")

    first_number = float(symbols[0])
    action = symbols[1]
    second_number = float(symbols[2])

    if action == "+":
        result = first_number + second_number
        print("Result:", result)
    elif action == "-":
        result = first_number - second_number
        print("Result:", result)
    else:
        raise ValueError("Use another action (+ or -).")

except ValueError as e:
    print("Error:", str(e))
except IndexError:
    print("Use space between numbers and action.")
