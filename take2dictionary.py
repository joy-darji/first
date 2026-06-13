import tkinter as tk
import requests

root = tk.Tk()
root.geometry("600x700")

label1 = tk.Label()
label1.pack()

textbox1 = tk.Entry()
textbox1.pack()


def emitests():
    accountnumber = textbox1.get() 
    data = requests.get(f"http://localhost:5000/api/loans/customer/{accountnumber}").json()


    if data["data"]["total_loans"]==0:
        label1.config(text = "he has no loans")

    else:
        data["data"]["total_loans"]==1



        roundfigure_loan_amount = int(data["data"]["loans"][0]["emi"])

        roundfigure1_loan_amount = int(data['data']["loans"][0]["tenure_months"])

        roundfigure2_loan_amount = int(data["data"]["loans"][0]["emi_paid"])

        roundfigure3_loan_amount = int(roundfigure1_loan_amount - roundfigure2_loan_amount)

        label1.config(text = f"the loan amount pending is {roundfigure3_loan_amount * roundfigure_loan_amount}")
     





button = tk.Button(text = "press here for get name", command = emitests)
button.pack()


root.mainloop()
