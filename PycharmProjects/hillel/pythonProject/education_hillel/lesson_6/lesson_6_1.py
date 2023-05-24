number = int(input("What's your number?: "))

def is_num_stepenof2(number):
    return ((number & (number - 1)) == 0)

if number == 0:
    print("Number is zero")
elif is_num_stepenof2(number):
    print("YES")
else:
    print("NO")
