names = ['john', 'marta', 'james', 'amanda', 'marianna']
top = 'NAME'.center(8, '*')
print(top)
for name in names:
    print(name.title().rjust(8))
