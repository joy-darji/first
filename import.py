

def dice():
    import random
    number = random.randint(1,6)
    return number

a = dice()
b = dice()
if a == 6 or b == 6:
    if a==6:
        temp=[a,"a"]
    else:
        temp=[b,"b"]
    print("congratulations you got",temp)

else:
    print("failed you got ",a,b)