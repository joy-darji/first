a = []

name = input("enter your name")
a.append(name)

surname = input("enter your surname")
a.append(surname)

city = input("enter your city")
a.append(city)

state = input("enter your state")
a.append(state)

country = input("enter your country")
a.append(country)

religion = input("enter your religion")
a.append(religion)

age = int(input("enter your age"))
a.append(age)

mobileno = int(input("enter your mobile number"))
a.append(mobileno)

s = set(a)
print(s)