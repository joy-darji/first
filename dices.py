def dice():
    import random
    number = random.randint(1,6)
    return number

rare = 0
while rare==0:

    a= dice()
    b= dice()
    c= dice()
    d= dice()
    if a==6 or b==6 or c==6 or d==6:
        if a==6:
            temp=["a",a]
        elif b==6:
            temp=["b",b]
        elif c==6:
            temp=["c",c]
        elif a == 6 and b == 6 and c == 6 and d == 6:
            print('rare event')
            rare = "done"
        else:
            temp=["d",d]
        print("congratulations you got",temp)

    else:
        print("failed you got",a,b,c,d)
    
    if rare == "done":
        print("rare")
        break