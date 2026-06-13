import requests

data = requests.get("http://192.168.1.39:5000/api/customers?page=1&per_page=500").json()
length = len(data["data"]["customers"])


def test(account_number):
    for i in range(0,length):
        a = data["data"]["customers"][i]["account_number"]
        if a == account_number:
            print(data["data"]["customers"][i]["name"])

def balance(account_number):
    for i in range(0,length):
        b = data["data"]["customers"][i]["account_number"]
        if b == account_number:
            print(data["data"]["customers"][i]["balance"])

def city(account_number):
    for i in range(0,length):
        c = data["data"]["customers"][i]["account_number"]
        if c == account_number:
            print(data["data"]["customers"][i]["city"])



while True:
    ac = input("enter account_number")
    choice = input(f"name\ncity\nbalance\nenter choice to work on {ac}: ")
    if choice == "name":
        test(ac)
    elif choice == "city":
        city(ac)
    elif choice == "balance":
        balance(ac)