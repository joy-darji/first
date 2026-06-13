import requests


data_calling = requests.get("http://localhost:5000/api/customers")

jsonconverted = data_calling.json()


for i in data_calling:
    if ["data"]["customers"][i]["balance"] < 2000:
        print(jsonconverted["data"]["customers"]["name"])
