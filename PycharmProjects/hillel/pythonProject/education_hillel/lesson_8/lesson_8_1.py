class ComplexNumber:
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def __add__(self, other):
        real_sum = self.real + other.real
        imaginary_sum = self.imaginary + other.imaginary
        return ComplexNumber(real_sum, imaginary_sum)

    def __sub__(self, other):
        real_diff = self.real - other.real
        imaginary_diff = self.imaginary - other.imaginary
        return ComplexNumber(real_diff, imaginary_diff)

    def __str__(self):
        if self.imaginary >= 0:
            return f"{self.real} + {self.imaginary}i"
        else:
            return f"{self.real} - {abs(self.imaginary)}i"


first_real_num = float(input("what's your first real number?:"))
first_imaginary_num = float(input("what's your first imaginary number?:"))
second_real_num = float(input("what's your second real number?:"))
second_imaginary_num = float(input("what's your second imaginary number?:"))

num1 = ComplexNumber(first_real_num, first_imaginary_num)
num2 = ComplexNumber(second_real_num, second_imaginary_num)
sum_result = num1 + num2
print(sum_result)


diff_result = num1 - num2
print(diff_result)
