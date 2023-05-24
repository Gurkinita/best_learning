my_list = ['FirstItem', 'FriendsList', 'MyTuple']

newList = []
for item in my_list:
    new_item = ''.join(['_'+i.lower()
    if i.isupper()
        else i for i in item]).lstrip('_')
    newList.append(new_item)
print(newList)