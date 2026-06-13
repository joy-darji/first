import requests

details = requests.get("http://192.168.1.39:5000/api/customers")    

jsonconverted = details.json()

length = len(jsonconverted["data"]["customers"])




for i in range(0,length):
    print(jsonconverted["data"]["customers"][i]["name"])
    print(jsonconverted["data"]["customers"][i]["balance"])


