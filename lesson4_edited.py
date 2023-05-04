# задание 1


names = ['john', 'marta', 'james', 'amanda', 'marianna']
top = 'NAME'.center(8, '*')
print(top)
for name in names:
    print(name.title().rjust(8))


# задание 2



my_list = ['FirstItem', 'FriendsList', 'MyTuple']

newList = []
for item in my_list:
    new_item = ''.join(['_'+i.lower()
    if i.isupper()
        else i for i in item]).lstrip('_')
    newList.append(new_item)
print(newList)

# задание 3

my_dict = {'Python':'Guido van Rossum', 'Java':'Sun Microsistems ', 'C#':'Anders Hejilsberg', 'Dylan':'Apple'}
for language, creator in my_dict.items():
    print(f"My favorite programming language is {language}. "
          f"It was created by {creator}.")
print('ща будет магия')
my_dict.pop('Java')
print(my_dict)


# задание 4


e2g = {'stork':'storch',
       'hawk':'falke',
       'woodpecker':'specht',
       'owl':'eule'}
new_dict = {'money':'geld',
            'honey':'honig'}
print(e2g)
print(e2g['owl'])

e2g.update(new_dict)
print(e2g)

my_list = list(e2g.items())
print(my_list)

# адание 5



subjects = {
            'science':{
                      'phisics': ['nuclear phisics', 'optics', 'thermodynamics'],
                      'computer science': {},
                      'biology': {}
            },
            'humanities':{},
            'public':{}
            }

for key in subjects['science'].keys():
    print(key)


for value in subjects['science']['phisics']:
    print(value)


# задание 6


my_dict = {}
for key in range(1, 16):
    my_dict[key] = key ** 2
print(my_dict)


