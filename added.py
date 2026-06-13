import pandas as pd

a =[ ]
try:
    dataset = pd.read_csv("data.csv",index=False)
    a = dataset.to_dict(orient = "records")
except:
    d = None
    d = pd.read_csv("data.csv")
    if d is None:
        a = [{"taskname":"test","description":"test","deadline":"test","completed":"test"}]
        dataset = pd.DataFrame(a)
        dataset.to_csv("data.csv",index=False)    
while True: 
    
    
    print("enter choice what you want to add delete or update or check")
    choice = input("enter choice:")
    
    if choice in("add","append","ADD"):
        taskname = input("enter name of task:")
        description = input("enter name of description:")
        deadline = input('enter deadline in days:')
        completed = (input("enter 1 if completed else enter 0 for not completed"))
        a.append({"taskname":taskname,"description":description,"deadline":deadline,"completed":completed})
        dataset = pd.DataFrame(a)
        dataset.to_csv("data.csv",mode="a",index=False,header=False)
        
        
    elif choice in("delete","DELETE","del","remove"):
        tasktd = (int(input("enter what you want to delete:")))
        del a[tasktd]
        dataset = pd.DataFrame(a)
        dataset.to_csv("data.csv",index=False)
        
        print("task deleted")


    elif choice in("update","UPDATE"):
        index = int(input("enter index to update"))
        taskname = input("enter new task:")
        description = input("enter new description")
        deadline = input("enter new deadline")
        completed = input("completed 1/0")

        a[index]["taskname"] = taskname
        a[index]["description"] = description
        a[index]["deadline"] = deadline
        a[index]["status"] = completed
        dataset = pd.DataFrame(a)
        dataset.to_csv("data.csv", index=False)
        
        

    elif choice in ["view","check","see"]:
        print("task_name  task_description  deadline  status")
        for i in range(len(a)):
            print(f"{a[i]["taskname"]}             {a[i]["description"]}             {a[i]["deadline"]}    {a[i]["completed"]}")