import requests

types_data= requests.get("http://192.168.1.39:5000/api/transactions/recent?limit=625").json()




for i in range(0,625):
    type_data = (types_data["data"]["recent_transactions"][i]["type"])

    print(type_data)
