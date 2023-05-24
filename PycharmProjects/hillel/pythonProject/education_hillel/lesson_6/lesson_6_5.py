def to_dict(lst):
    my_dict = {}
    for i, item in enumerate(lst):
        my_dict[item] = item
    return my_dict

my_list = input("what's your list? (use space between): ").split()

result_dict = to_dict(my_list)
print(result_dict)
