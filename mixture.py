name = input("enter your name")
surname = input("enter your surname")
age = int(input("enter yoyr age"))
city = input("enter your city")

namelist=[]
namelist.append(name)

citytuple={city}

data={}
data[name] = surname

print("list:",namelist)
print("tuple",citytuple)
print("dictionary",data)


# dictionary merge with name and account type and balance
# print account with who's balance is less than 1000 dollars
# updat account balance with -10 dollar service fees