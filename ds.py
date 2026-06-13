import pandas as pd

students_details = pd.read_csv("ds.csv")

def phone_number(Phonenumber):
    print(students_details[students_details["phoneno"] == Phonenumber])

while True:
    Phonenumber = int(input("enter phonenumber:"))
    phone_number(Phonenumber)