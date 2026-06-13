import pandas as pd

a = []

taskname = input("enter name of task")
description = input("enter name of description")
deadline = input("enter deadline in days")
completed = input("enter 0 if completed and enter 1 if not completed")

a.append({"taskname":taskname,"description":description,"deadline":deadline,"completed":completed})

dataset = pd.DataFrame(a)
dataset.to_csv((f"tasks/{taskname}.csv"),mode ="a",index =False,header = True)