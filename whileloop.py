abc = []
def apnd():   
    task = input("enter task")
    abc.append(task)
    print(abc)

def delete():
    print(abc)
    deleteno = int(input("enter index"))
    del abc[deleteno]
    print(abc)

def update():
    print(abc)
    update = int(input("select your index"))
    newtask=input("enter new task: ")
    abc[update]= newtask
    print (abc)

def full_list():
    print(abc)


while True:
    choices = int(input("enter choice"))
    if choices == 1:
        apnd()
    elif choices == 2:
        delete()
    elif choices == 3:
        update()
    elif choices == 4:
        full_list()

