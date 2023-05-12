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
