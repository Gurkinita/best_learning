class DiscriminantError(Exception):
    pass

a = float(input("Enter a: "))
b = float(input("Enter b: "))
c = float(input("Enter c: "))

D = b**2 - 4*a*c

try:
    if D < 0:
        raise DiscriminantError("Дискриминант отрицательный")

    sqrt_D = D**0.5
    x1 = (-b + sqrt_D) / (2*a)
    print("x1 =", x1)

except DiscriminantError as e:
    print("Ошибка:", str(e))
