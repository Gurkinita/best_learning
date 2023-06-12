import argparse

class DiscriminantError(Exception):
    pass

def calculate_quadratic_equation(a, b, c):
    D = b**2 - 4*a*c

    try:
        if D < 0:
            raise DiscriminantError("Negative discriminant")

        sqrt_D = D**0.5
        x1 = (-b + sqrt_D) / (2*a)
        print("x1 =", x1)

    except DiscriminantError as e:
        print("Error:", str(e))

def main():
    parser = argparse.ArgumentParser(description="Quadratic equation calculation")
    parser.add_argument("-a", type=float, default=0, help="Coefficient a")
    parser.add_argument("-b", type=float, required=True, help="Coefficient b")
    parser.add_argument("-c", type=float, required=True, help="Coefficient c")
    args = parser.parse_args()

    calculate_quadratic_equation(args.a, args.b, args.c)

if __name__ == "__main__":
    main()
