import requests

calldata = requests.get("http://192.168.1.39:5000/api/customers")


jay = calldata.json()



for i in range(0,20):
    occupation1 = jay["data"]["customers"][i]["occupation"]

    if occupation1 == "Student":
        print(occupation1)