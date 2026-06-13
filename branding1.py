import pandas as pd

class shoeanalyze:

    def __init__(self,country):

        data = pd.read_csv("shoes_sales_dataset.csv")
        self.country = country 
        self.countrydata = data[data["Country"]== self.country]

    

    def branding(self,brand):

        self.brand = brand
        branddata = self.countrydata[self.countrydata["Brand"]== self.brand]
        return branddata
        
    def shoe_types(self,shoetype):
        self.shoetype = shoetype
        shoetype_data = self.countrydata[self.countrydata["Shoe_Type"]== self.shoetype]
        return shoetype_data
    
Country = input("enter country")

COUNTRY = shoeanalyze(Country)

Brandname = input("enter brand name")

branddata = COUNTRY.branding(Brandname)

branddata.to_csv(f"{Country}_{Brandname}.csv")
print("file generated successfully")








        