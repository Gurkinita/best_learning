my_dict = {'Python':'Guido van Rossum', 'Java':'Sun Microsistems ', 'C#':'Anders Hejilsberg', 'Dylan':'Apple'}
for language, creator in my_dict.items():
    print(f"My favorite programming language is {language}. "
          f"It was created by {creator}.")
print('ща будет магия')
my_dict.pop('Java')
print(my_dict)
