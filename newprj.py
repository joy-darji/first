import smtplib
from email.message import EmailMessage
import random
import requests
import json


add_doc = "http://127.0.0.1:7000/add_doctor"
add_patient = "http://127.0.0.1:7000/add_patient"
add_staff = "http://127.0.0.1:7000/add_staff"
add_equipment = "http://127.0.0.1:7000/add_equipment"
put_equipment = "http://127.0.0.1:7000/take_equipment"


while True:
    print("\npress 1 for add patient\npress 2 for add doctor\npress 3 for add staff\npress 4 for details\npress 5 for add equipments\npress 6 for put equipments")
    choice = int(input("enter your choice"))

    if choice == 1:

        address = input("dear customer enter your address:")
        age = int(input("dear customer enter your age:"))
        gender = (input("dear customer enter your gender:"))
        name = (input("dear customer enter your name:"))
        phone_no = int(input("dear customer enter your phone number:"))
        email = input("enter mail:")
        num3 = random.randint(1000,9999)


        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.login("darjijay017@gmail.com", "diuwkupwrnoxbogy")
        server.sendmail("darjijay017@gmail.com",email, (f"Hello your otp is {num3} for registering as an patient"))
        print("Email sent successfully!")



        datapatient = {"address":address,"age":age,"gender":gender,"name":name,"phone":phone_no}


        for i in range(5):

            otpuser = int(input("Enter opt:"))
            if otpuser == num3:
                data3 = requests.post(add_patient,json = datapatient)
                print(data3.json())
                break
            else:
                print("incorrect otp please try again") 
                



    elif choice == 2:

        num = random.randint(1000,9999)
            
        name = (input("dear doctor enter your name"))
        phone_no = int(input("dear doctor enter your phone"))
        specilization = input("dear doctor enter your specialization")
        docemail = input("dear doctor enter your email")


        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.login("darjijay017@gmail.com", "diuwkupwrnoxbogy")
        server.sendmail("darjijay017@gmail.com",docemail, (f"Hello doctor your otp is {num}"))
        print("Email sent successfully!")

        datadoc = {"email":docemail,"name":name,"phone":phone_no,"specialization":specilization}

        for i in range(5):

            otpuser = int(input("Enter OTP:"))
            if otpuser == num:
                data = requests.post(add_doc,json = datadoc)
                print(data.json())
                break
            else:
                print("incorrect otp")
                
                

    elif choice == 3:

        num2 = random.randint(1000,9999)


        department = input("dear staff member enter your department")
        name = input("dear staff member enter your name")
        phone = int(input("dear staff member enter your phone number"))
        role = input("dear staff member enter your role")
        staff_id = input("dear staff member enter your id")
        staff_email = input("dear staff member enter your email address")



        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.login("darjijay017@gmail.com", "diuwkupwrnoxbogy")
        server.sendmail("darjijay017@gmail.com",staff_email, (f"Hello your otp is {num2} for registering as an patient"))
        print("Email sent successfully!")

        datastaff = {"department":department,"name":name,"phone":phone,"role":role,"staff_id":staff_id}

        for i in range(5):

            otpuser = int(input("Enter opt:"))
            if otpuser == num2 :
                data1 = requests.post(add_staff,json = datastaff)
                print(data1.json())
                break

            else:
                print("incorrect otp")
                



    elif choice == 5:

        name = input("enter your equipment name")
        quantity = int(input("enter your quantity"))
        status = input("enter status")

        data_equipment = {"name":name,"quantity":quantity,"status":status}


        data5 = requests.post(add_equipment,json = data_equipment)
        print(data5.json())

    elif choice == 6:

        equipment_id = input("enter equipment id that you want to put")
        quantity_to_take = int(input("enter quantity that you want to take"))

        data = requests.put("http://127.0.0.1:7000/take_equipment",json = {"equipment_id":equipment_id,"quantity_to_take":quantity_to_take})
        print(data.json())


    # elif choice == 4:
    #     requests.get("")
    else:
        print("invalid choice")
