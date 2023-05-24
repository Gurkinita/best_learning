your_text = input("What's your text?: ")
my_word = your_text[:4]
new_text = your_text.replace('abc', 'www')
new_final = 'zzz'
if 'abc' in my_word:
    print(new_text)
else:
    print(your_text + new_final)
