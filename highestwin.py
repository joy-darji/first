import pandas as pd

data = pd.read_csv("bgmi_dataset.csv")

pro_player = data[data["wins"] == data["matches_played"]]

print(pro_player["player_name"])