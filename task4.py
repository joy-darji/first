import pandas as pd 

data = pd.read_csv("bgmi_dataset.csv")

while True:

    name_search = input("enter player name")


    if data["player_name"].str.contains(name_search).any():
        player_data = data[data["player_name"] == name_search]
        print(f"the player is {name_search} and his stats are {player_data["kills"].values[0]}")

    elif name_search == "quit":
        break

    else:
        print("player not found")