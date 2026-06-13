import requests

morethan1lakh = requests.get("http://192.168.1.39:5000/api/transactions/recent?limit=625").json()

for i in range(0,625):
    morethan = (morethan1lakh["data"]["recent_transactions"][i]["amount"])

    name = morethan1lakh["data"]["recent_transactions"][i]
    amount = i["amount"   ]

    if amount > 100000:
        print(name,amount)