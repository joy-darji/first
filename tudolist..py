tasklist=[]
while True:
    choice=int(input("enter your choice"))

    if choice==1:
        task =(input("enter task"))
        tasklist.append(task)
        print(tasklist)

    elif choice==2:
        task=int(input("enter task"))
        del tasklist[task]
        print(tasklist)
