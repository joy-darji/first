import pandas as pd

data = pd.read_csv("bgmi_dataset.csv")

data1 = data[data["tier"] == "diamond"]

data1 = data1.loc[:, ["player_name", "kills", "kd_ratio"]]

print(data1)