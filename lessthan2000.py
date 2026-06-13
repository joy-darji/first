import requests


data = requests.get("http://localhost:5000/api/customers").json()

names = []


for i in range(0,20):
    balance = int(data["data"]["customers"][i]["balance"])
    if balance<2000:
        names.append(f"{data["data"]["customers"][i]["name"]},{data["data"]["customers"][i]["balance"]}")

print(names)