import requests

calleddata = requests.get("http://192.168.1.39:5000/api/customers")

jsonconverted = calleddata.json()

length = len(jsonconverted["data"]["customers"])
total = 0

cityname= input("enter your city name:")
for i in range(1,length):
    city = jsonconverted["data"]["customers"][i]["city"]
    if city == cityname:
        bal = jsonconverted["data"]["customers"][i]["balance"]
        total = total + bal

print(total)
