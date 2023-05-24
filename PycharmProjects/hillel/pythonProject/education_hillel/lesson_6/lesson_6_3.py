from math import sqrt

def is_prime(number):
    if number < 2 or number > 1000:
        print("Invalid input")
        return False

    for i in range(2, int(sqrt(number)) + 1):
        if number % i == 0:
            return False

    return True

number = float(input("What's your number from 2 to 1000?: "))

if is_prime(number):
    print("True")
else:
    print("False")
