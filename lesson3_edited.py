# задание 1


your_word = input('whats your word?:')
strait = (your_word[:])
back = (your_word[::-1])

if strait == back:
    print('+')
else:
    print("-")


# задание 2
your_text = input("whats your text?:")

your_word = input("what are we looking for?:")

if your_word in your_text:
    print('YES')
else:
    print("No")

# задание 3

your_text = input("What's your text?: ")
my_word = your_text[:4]
new_text = your_text.replace('abc', 'www')
new_final = 'zzz'
if 'abc' in my_word:
    print(new_text)
else:
    print(your_text + new_final)



# задание 4


your_email = input("whats your email?:")

your_simbol = '@'

if your_simbol in your_email:
    print('YES')
else:
    print("No")

#задание 5



your_text = input('whats your text?:')
your_list = your_text.split(" ")
your_elements = len(your_list)

if your_elements >= 3:
    print(your_list[-3:])
else:
    print('you need 3 and more words, you have only ' + str(your_elements))

