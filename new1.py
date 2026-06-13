import requests
calldata = requests.get("http://192.168.1.39:5000/api/customers")

jsonconverted = calldata.json()

length = len(jsonconverted["data"]["customers"])

for i in range(0,length)



