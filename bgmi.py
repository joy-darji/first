import pandas as pd 

class player:

    def __init__(self,name,tier,kills,match_played,wins):

        data = pd.read_csv("bgmi_dataset.csv")

        self.name = name
        self.tier = tier
        self.kills = kills
        self.match_played = match_played
        self.wins = wins

    def win_rate(self):
        return((self.wins/self.match_played)*100,2)
    
    def display_stats(self):
        print(f"player name : {self.name}")
        print(f"player tier : {self.tier}")
        print(f"player kills : {self.killa}")
        print(f"playe the match played  ; {self.match_played}")
        print(f"player that wins the match : {self.wins}")



