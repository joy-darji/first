import pandas as pd 

data = pd.read_csv("bgmi_dataset.csv")

a = data.iloc[0:10,0:4]

print(a)