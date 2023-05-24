while True:
    a = int(input("What will we do? if + press1, if - press 2, if * press 3, if / press4: "))
    if a in [1, 2, 3, 4]:
        break
    else:
        print("Try again")


num1 = float(input("num1 :"))
num2 = float(input("num2 :"))

if a == 1:
    print (num1+num2)

elif a == 2:
     print (num1-num2)

elif a == 3:
    print (num1*num2)

elif a == 4:
    print (num1/num2)