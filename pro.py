tasklist=[]

choice=int(input(" 1 for add \n 2 for delete \n 3 for delete a choice \n enter choice"))
 
if choice==1:
    task=(input("enter task"))
    tasklist=(input("enter that you want to append"))
    tasklist.append("")
    print(task)


elif choice==2:
    task=(input("enter task "))
    location=((input("enter that you want to delete location")))
    del tasklist[task] 
    print(tasklist)




    


      
    