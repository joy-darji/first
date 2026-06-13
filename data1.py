import requests
customerdata = requests.get("http://localhost:5000/api/customers?page=1&per_page=1000").json()
apidata = requests.get("http://localhost:5000/api/transactions/recent?limit=500").json()
names = []
# print(apidata["data"])
length = len(apidata["data"]["recent_transactions"])
for i in range(0,length):
    amt = float(apidata["data"]["recent_transactions"][i]["amount"])
    if amt==100:
        accountno = (apidata["data"]["recent_transactions"][i]["from_account"])
        for j in range(0,100):
            if accountno == customerdata["data"]["customers"][j]["account_number"]:
                name = customerdata["data"]["customers"][j]["name"]
                names.append(name)
            
print(names)