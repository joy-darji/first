import tkinter as tk
import requests

root = tk.Tk()
root.geometry("600x700")

label1 = tk.Label()
label1.pack()

label2 = tk.Label()
label2.pack()

label3 = tk.Label()
label3.pack()

label4 = tk.Label()
label4.pack()


textbox1 = tk.Entry()
textbox1.pack()

def tests():
    accountnumber = textbox1.get()
    data = requests.get(f"http://localhost:5000/api/loans/customer/{accountnumber}").json()

    if  data["data"]["total_loans"]==0:
        label1.config(text = "he has no loans")

    else:
        loanemi = data["data"]["loans"][0]["emi"]
        label1.config(text = (f"he has loan and EMI is : {loanemi}"))



button = tk.Button(text = "press here for get name", command = tests)
button.pack()


root.mainloop()