import smtplib
from email.message import EmailMessage
import random


num = random.randint(4000,9000)

# # 1. Create the message
# msg = EmailMessage()
# msg.set_content("Hello! This iksdfpodskposdkfspos a test email sent from Python.")
# msg['Subject'] = 'Test Email'
# msg['From'] = "anmolnelson@gmail.com"
# msg['To'] = "anmolnelson@gmail.com"

# 2. Connect and send

    # Use port 465 for SSL (secure from the start)
# with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:

server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
server.login(".com", "")
server.sendmail("anmolnelson@gmail.com","anmolnelson@gmail.com", (f"Hello your otp is {num}"))
print("Email sent successfully!")


while True:
    otpuser = input("Enter opt:")
    if otpuser == num:
        print("success")
    else:
        print("incorrect otp")
        continue
    
    
    
# healthcare management system
# patient admission form: name, number, age, date
# doctor: name, degree, yoe, category
# staff: name, designation, salary, yoe, 

staff  = {}

staff[name] = {"name":name,"age":age, "yoe":yoe}