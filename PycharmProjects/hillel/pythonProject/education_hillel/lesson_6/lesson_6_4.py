
def change_list(my_list, a, b):
    my_list[a], my_list[b] = my_list[b], my_list[a]

my_list = input("what's your list?(use space between): ").split()

change_list(my_list, 0, -1)

print(my_list)



