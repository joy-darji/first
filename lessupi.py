import requests

upi_data = requests.get("http://localhost:5000/api/transactions/recent?limit=625").json()
length = len(upi_data["data"]["recent_transactions"])
total = 0


UPI = 0
NEFT = 0
for i in range(0,length):
    type = (upi_data["data"]["recent_transactions"][i]["type"])
    amount=(upi_data["data"]["recent_transactions"][i]["amount"])
    if type == "NEFT":
        NEFT = NEFT+1
    elif type == "UPI":
        UPI = UPI+1

print(f"UPI transactions are: {UPI} ")
print(f"NEFT transactions are: {NEFT} ")



