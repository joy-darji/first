import requests

def get_age(accountno):
    data = requests.get(f"http://localhost:5000/api/customers/{accountno}").json()
    dob = data["data"]["date_of_birth"]
    doby = int(dob[0:4:1])
    age = 2026 - doby 
    return age

accprefix = "SBIN"
accsuffix = 1000000001
oldestinfo = []
allage = []
mnth = 0
maxagename = ""
hisage = 0
try:
    while True:
        accountno = accprefix + str(accsuffix)
        data = requests.get(f"http://localhost:5000/api/customers/{accountno}").json()
        age = get_age(accountno)
        allage.append(age)
        if age==76:
            name = data["data"]["name"]   
            dob = data["data"]["date_of_birth"]
            balance = data["data"]["balance"]
            year = int(dob[0:4])
            month = int(dob[5:7])
            if mnth < month:
                mnth = month
                maxagename = name
                hisage = age
            
            
            d = {name:[{"balance":balance,"age":age,"year":year,"month":month}]}
            childinfo.append(d)
            

        accsuffix = accsuffix+1 
except:
    print("ended")

print(oldestinfo)



print(maxagename, "is oldest customer with age", hisage)