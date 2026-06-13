def pricechecker(enginecc):

    enginecc = input("enter your car cc")

    if enginecc <= 1000:
        print("4 lakh to 7 lakh")

    elif 1000 <= 1500:
        print("9 lakh to 13 lakh")

    elif 1500 <= 2000:
        print("15 lakh to 53 lakh")

    else:
        print("70 lakh to 10 crore")


class cars:

    def supercar():
        horsepower = int(input("enter horsepower"))
        car_name = input("enter car name")
        enginecc = int(input("enter car cc"))

        price = pricechecker(enginecc)
        print("supercar name:", car_name)
        print("horsepower:", horsepower)
        print("enginecc:", enginecc)
        print("price range:", price)

    def sportscar():

        horsepower = int(input("enter horsepower"))
        seats = int(input("enter seats"))
        mileage = int(input("enter the mileage"))
        enginecc = int(input("enter car cc"))

        price = pricechecker(enginecc)
        print("horsepower:", horsepower)
        print("seats:", seats)
        print("mileage:", mileage)
        print("enginecc:", enginecc)

    def offroader():

        totalwheels = int(input("how many wheels in this offroader"))
        horsepower = int(input("enter the horsepower"))
        enginecc = int(input("enter your engine cc"))
        AWD = input("is this offroadef all whell drive Yes/No")

        price = pricechecker(enginecc)
        print("totalwheels:", totalwheels)
        print("horsepower:", horsepower)
        print("enginecc:", enginecc)
        print("AWD:", AWD)

    supercar()
    sportscar()
    offroader()
