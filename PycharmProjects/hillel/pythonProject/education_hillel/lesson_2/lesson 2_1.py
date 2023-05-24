while True:
    a = int(input("if you wanna change USD to UAH press 1, if you wanna change UAH to EUR press 2, if you wanna change "
                  "EUR to UAH press 3: "))
    if a in [1, 2, 3]:
        break
    else:
        print("Try again")


b = int(input("how manu you wanna change :"))


if a == 1:
    print (b*38)

elif a == 2:
    print (b/42)

elif a == 3:
    print (b*42)
