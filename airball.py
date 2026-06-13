import requests

def get_age(accountno):
    data = requests.get(f"http://localhost:5000/api/customers/{accountno}").json()
    dob = data["data"]["date_of_birth"]
    doby = int(dob[0:4:1])
    age = 2026 - doby 
    return age
