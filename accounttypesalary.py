import requests

accountprefix = "SBIN"
accountsuffix = 1000000001

data = []
salary = 0
balance = 0
total_salary_balance = 0

for i in range(0,100):
    accountnumber = accountprefix+str(accountsuffix)
    fulldata = requests.get(f"http://localhost:5000/api/customers/{accountnumber}").json()
    accounttype = fulldata["data"]["account_type"]
    balance = fulldata["data"]["balance"]
    if accounttype == "Salary":
        salary +=1
        total_salary_balance +=balance

    
    data.append(accounttype)
    accountsuffix = accountsuffix+1



    
print({"Salary":salary,"totalbal":total_salary_balance})



