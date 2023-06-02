import math


class Dot:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Triangle:
    def __init__(self, dot1, dot2, dot3):
        self.dot1 = dot1
        self.dot2 = dot2
        self.dot3 = dot3

    def calculate_area(self):
        side1 = math.sqrt((self.dot2.x - self.dot1.x) ** 2 + (self.dot2.y - self.dot1.y) ** 2)
        side2 = math.sqrt((self.dot3.x - self.dot2.x) ** 2 + (self.dot3.y - self.dot2.y) ** 2)
        side3 = math.sqrt((self.dot1.x - self.dot3.x) ** 2 + (self.dot1.y - self.dot3.y) ** 2)

        if self.is_valid_triangle(side1, side2, side3):
            semiperimeter = (side1 + side2 + side3) / 2
            area = math.sqrt(
                semiperimeter * (semiperimeter - side1) * (semiperimeter - side2) * (semiperimeter - side3))
            return area
        else:
            print("Can't calculate triangle area. Try again")
            return None

    def is_valid_triangle(self, side1, side2, side3):
        return side1 + side2 > side3 and side2 + side3 > side1 and side3 + side1 > side2


class Square:
    def __init__(self, dot1, dot2, dot3, dot4):
        self.dot1 = dot1
        self.dot2 = dot2
        self.dot3 = dot3
        self.dot4 = dot4

    def calculate_area(self):
        side1 = math.sqrt((self.dot2.x - self.dot1.x) ** 2 + (self.dot2.y - self.dot1.y) ** 2)
        side2 = math.sqrt((self.dot3.x - self.dot2.x) ** 2 + (self.dot3.y - self.dot2.y) ** 2)
        side3 = math.sqrt((self.dot4.x - self.dot3.x) ** 2 + (self.dot4.y - self.dot3.y) ** 2)
        side4 = math.sqrt((self.dot1.x - self.dot4.x) ** 2 + (self.dot1.y - self.dot4.y) ** 2)

        if self.is_valid_square(side1, side2, side3, side4):
            area = side1 * side2
            return area
        else:
            print("Can't calculate square area. Try again")
            return None

    def is_valid_square(self, side1, side2, side3, side4):
        return side1 == side2 == side3 == side4 and side1 > 0



first_x = float(input("what's your first X coordination?:"))
first_y = float(input("what's your first Y coordination?:"))
second_x = float(input("what's your second X coordination?:"))
second_y = float(input("what's your second Y coordination?:"))
third_x = float(input("what's your third X coordination?:"))
third_y = float(input("what's your third Y coordination?:"))
fourth_x = float(input("what's your fourth X coordination?:"))
fourth_y = float(input("what's your fourth Y coordination?:"))

dot1 = Dot(first_x, first_y)
dot2 = Dot(second_x, second_y)
dot3 = Dot(third_x, third_y)
dot4 = Dot(fourth_x, fourth_y)

triangle = Triangle(dot1, dot2, dot3)
triangle_area = triangle.calculate_area()
print("Triangle area is:", triangle_area)

square = Square(dot1, dot2, dot3, dot4)
square_area = square.calculate_area()
print("square area is:", square_area)