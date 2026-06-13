fullmarks = 100

maths=int(input("enter python marks"))
python=int(input("enter maths marks"))
if python > 90 or maths > 90: 
    print("A")

elif python > 80 or maths > 80:
    print("B")

elif python > 70 or maths > 70:
    print("C")

elif python > 60 or maths > 60:
    print("D")

elif python > 50 or maths > 50:
    print("E")

elif python > 40 or maths > 40:
    print("EE")

else:
    print("fail")