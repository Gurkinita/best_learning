# main.py
from lesson_6.lesson_6_1 import is_num_stepenof2
from lesson_6.lesson_6_2 import Square
from lesson_6.lesson_6_3 import is_prime
from lesson_6.lesson_6_4 import change_list
from lesson_6.lesson_6_5 import to_dict
from lesson_6.lesson_6_6 import sum_range

def main():

    result = is_num_stepenof2()
    print(result)

    result = Square()
    print(result)

    result = is_prime()
    print(result)

    result = change_list()
    print(result)

    result = to_dict()
    print(result)

    result = sum_range()
    print(result)

if __name__ == '__main__':
    main()
