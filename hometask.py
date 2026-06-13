def checkage(age):
    if age <= 18:
        print("teenage")
    else:
        print("adult")

age = int(input("enter age "))

checkage(age)