import pandas as pd

customers_details = pd.read_csv("ecommerce_churn_500_rows.csv")

while True:
    choice1 = input("\nchoices are:\nAge\nGender\nTotal_Spend\nAverage_Order_Value\nPurchase_Frequency\nLast_Purchase_Days\nCustomer_Rating\nComplaint_Raised\nReturn_Count\nChurn\nselect the column which you want to operate:")
    if choice1 in["age","AGE","Age","AgE","aGE","AgE"]:
        choice_age = input("\n1.greater_than\n2.less_than\n3.equals_to\nenter choice for Age")
        if choice_age =="1":
            age = input("enter age for get greater than data")
            print(customers_details[customers_details["Age"]>int(age)])
        elif choice_age == "2":
            age = input("enter age for get less than data")
            print(customers_details[customers_details["Age"]<int(age)])
        elif choice_age == "3":
            age = input("enter age for get equals data")
            print(customers_details[customers_details["Age"]==int(age)])

    elif choice1 in["total spend","TOTAL SPEND","tsp","TSP"]:
        total_spend = input("\n1.greater_than\n2.less_than\n3.equals_to\nenter choice for total spend")
        if total_spend =="1":
            tsp = input("enter tsp for get greater than data")
            print(customers_details[customers_details["Total_Spend"]>int(tsp)])
        elif total_spend =="2":
            tsp = input("enter tsp for get less than data")
            print(customers_details[customers_details["Total_Spend"]>int(tsp)])
        elif total_spend =="3":
            tsp = input("enter tsp for get equals data")
            print(customers_details[customers_details["Total_Spend"]>int(tsp)])

    elif choice1 in["avg order value","AVG ORDER VALUE","average order value","AVERAGE ORDER VALUE"]:
        avg_ord_value = input("\n1.greater_than\n2.less_than\n3.equals_to\nenter choice for average order value")
        if avg_ord_value == "1":
            aov = input("enter aov for get greater than data")
            print(customers_details[customers_details["Average_Order_Value"]>int(aov)])
        elif avg_ord_value == "2":
            aov = input("enter aov for get less than data")
            print(customers_details[customers_details["Average_Order_Value"]>int(aov)])
        elif avg_ord_value == "3":
             aov = input("enter aov for equal data")
             print(customers_details[customers_details["Average_Order_Value"]>int(aov)])

