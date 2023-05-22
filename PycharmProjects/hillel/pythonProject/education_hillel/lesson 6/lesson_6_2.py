import math

side = float(input("What's your square side?: "))

def Square(side):
    perimeter = side * 4
    square_area = side ** 2
    diagonal = math.sqrt(2 * (side ** 2))
    my_tuple = ("Perimeter is:", perimeter, "Square is:", square_area, "Diagonal is:", diagonal)
    print(my_tuple)

Square(side)
