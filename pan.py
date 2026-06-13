import pandas as pd

student_details = pd.read_csv("data.csv")

print(type(student_details["Permanentloc"]))
