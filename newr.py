class mileagecalculator:
    def __init__(self,carname,petrol,kmdriven):

        self.carname = carname
        self.petrol = petrol
        self.kmdriven = kmdriven



    def totalmileage(self,):
        milage = self.kmdriven / self.petrol
        print(f"{self.carname} mileage is {milage}")


car = mileagecalculator("lambo",20,100)
print(car.totalmileage())