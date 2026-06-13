import pandas as pd 
data = pd.read_csv("data.csv")

todolist = []
while True:

    print("enter choice what you want to add delete or update or check")
    choice = input("enter choice:")

    if choice in["add","ADD"]:
        taskname = input("enter your task:")
        description = input("enter your description:")
        deadline = input("enter deadline in days:")
        completed = input("enter 1 if completed of enter 0 if not completed")
        todolist.append({"taskname":taskname,"description":description,"deadline":deadline,"completed_or_not":completed})

        if len()