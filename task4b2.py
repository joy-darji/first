import pandas as pd 

data = pd.read_csv("bgmi_dataset.csv")

player_win = data[data["wins"] > 20]

player_kd = data[data["kd_ratio"] > 5]

print(player_win)
print(player_kd)