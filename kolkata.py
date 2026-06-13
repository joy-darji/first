import requests
kolkatadata = requests.get("http://192.168.1.39:5000/api/customers?page=1&per_page=1000").json()

length = len(kolkatadata["data"]["customers"])

city = []

def citychecker(i):
    city = (kolkatadata["data"]["customers"][i]["city"])
    balance = (kolkatadata["data"]["customers"][i]["balance"])


    return city,balance
for i in range(1,length):
    city,balance = citychecker(i) 

    if balance>= 1000 and city=="Kolkata":
        print(kolkatadata["data"]["customers"][i]['name'])

        
        
