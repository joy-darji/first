choices = int(input("enter your choice"))

def day_counter():
    born_year = int(input("enter born year"))
    age = 2026 - born_year
    age = age * 365
    print(f"you are {age} days old")

def hour_counter():
    born_year = int(input("enter born year"))
    age = 2026 - born_year
    age = age * 365 * 24
    print(f"you are {age} hours old")

def month_counter():
    born_year = int(input("enter born year"))
    age = 2026 - born_year
    age = age * 12
    print(f"you are {age} months old")


if choices == 1:
    day_counter()
elif choices == 2:
    hour_counter()
elif choices == 3:
    month_counter()