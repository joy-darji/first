import requests

accountprefix = "SBIN"
accountsuffix = 1000000001

data = []
nri = 0
balance = 0
total_nri_balance = 0

for i in range(0,100):
    accountnumber = accountprefix+str(accountsuffix)
    fulldata = requests.get(f"http://192.168.1.39:5000/api/customers/{accountnumber}").json()
    occupation = fulldata["data"]["account_type"]
    balance = fulldata["data"]["balance"]
    if occupation == "NRI":
        nri +=1
        total_nri_balance +=balance

    
    data.append(occupation)
    accountsuffix = accountsuffix+1



    
print({"NRI":nri,"totalbal":total_nri_balance})



