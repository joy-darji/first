import requests

morethan2lakh = requests.get("http://192.168.1.39:5000/api/transactions/recent?limit=625").json()

for i in range(0,625):
    morethan = (morethan2lakh["data"]["recent_transactions"][i]["amount"])

    name = i["name"]
    amount = i['amount']

    if amount > 200000:
        print(name,amount)