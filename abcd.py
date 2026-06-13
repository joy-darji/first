choices = int(input("enter your choice"))

def addition():
    a = int(input("enter a:"))
    b = int(input("enter b:"))
    print(a+b)

def substraction():
    a = int(input("enter a:"))
    b = int(input("enter b:"))
    print(a-b)

def multiplication():
    a = int(input("enter a:"))
    b = int(input("enter b:"))
    print(a*b)

def modulus():
    a = int(input("enter a:"))
    b = int(input("enter b:"))
    print(a%b)


def day_counter():
    born_year = int(input("enter born year"))
    age = 2026 - born_year
    age = age * 365
    print(f"you are {age} days old")

if choices == 1:
    addition()
elif choices == 2:
    substraction()
elif choices == 3:
    multiplication()
elif choices == 4:
    modulus()
elif choices == 5:
    day_counter()
 