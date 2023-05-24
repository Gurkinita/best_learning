your_text = input('whats your text?:')
your_list = your_text.split(" ")
your_elements = len(your_list)

if your_elements >= 3:
    print(your_list[-3:])
else:
    print('you need 3 and more words, you have only ' + str(your_elements))