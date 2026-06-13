import pandas as pd

data = pd.read_csv("bgmi_dataset.csv")


head_percent = data[data["headshot_pct"] > 50]

print(head_percent)