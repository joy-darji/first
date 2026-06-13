import pandas as pd

data = pd.read_csv("bgmi_dataset.csv")

data["loses"] = data["matches_played"] - data["wins"]

newdata = data.sort_values(by = "loses",ascending = False) 



print(newdata)