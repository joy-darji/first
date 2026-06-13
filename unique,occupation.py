import requests

accprefix = "SBIN"
accsuffix = 1000000001
data = []
occupation = {}
student = 0
retired = 0
professional = 0
homemaker = 0
service = 0
for i in range(0,100):
    accountnumber = accprefix+str(accsuffix)

    wholedata = requests.get(f"http://192.168.1.39:5000/api/customers/{accountnumber}").json()
    occupation = wholedata["data"]["occupation"]
    balance = wholedata["data"]["balance"]
    if occupation == "Student":
        student +=1
    elif occupation == "Professional":
        professional +=1
    elif occupation == "Retired":
        retired +=1
    elif occupation == "Homemaker":
        homemaker +=1
    elif occupation == "Service":
        service +=1

    data.append(occupation)
    accsuffix = accsuffix+1


    
print({"Student":student})
print({"Professional":professional})
print({"Retired":retired})
print({"Homemaker":homemaker})
print({"Service":service})


print(wholedata["data"][""])
