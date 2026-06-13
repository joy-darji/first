import requests
customerdata = requests.get("http://localhost:5000/api/customers?page=1&per_page=1000").json()

length = len((customerdata["data"]["customers"]))

data = []

def balancechecker(i):
    name = customerdata["data"]["customers"][i]["name"]
    balance = customerdata["data"]["customers"][i]["balance"]
    return name,balance

for i in range(1,length):
    name,balance = balancechecker(i)
    if len(name)<=11:
        print(name)