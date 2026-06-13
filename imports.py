import requests
data= requests.get("http://192.168.1.39:5000/api/dashboard/summary").json()
print(data["data"])