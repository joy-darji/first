choice = int(input("enter your choice"))

if choice ==1:
    num = int(input("enter number for table"))

    for i in range(1,21):
        print(num,"x",i,"=", num*i)

elif choice == 2:
    num = int(input("enter a number"))

    if  num%2==0:
        print("the number is even")
    else:
        print("the number is odd")

 

else:
    print("invalid choice")