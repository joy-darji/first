import pandas as pd

class shoeanalyze:

    def __init__(self,prices):

        data = pd.read_csv("shoes_sales_dataset.csv")
        self.prices = prices
        self.pricedata = data[data["price"]>= 100]

    def country(self,country):
        self.country = self.country
        country_data = self.pricedata[self.pricedata["Country"]== self.counry]
    def brand(self,brand):

        self.brand = brand
        branddata = self.pricedata[self.pricedata["Brand"]== self.brand]
        return branddata
    
    def shoe_types(self,shoetype):
        self.shoetype = shoetype
        shoetype_data = self.pricedata[self.pricedata["Shoe_Type"]== self.shoetype]
        return shoetype_data
    

PRICES =  shoeanalyze(100)

counry_name = input("enter country name")
PRICES.country(counry_name)

brandname = input("enter brand name")
PRICES.brand(brandname)

shoetype = input("enter shoe type")
PRICES.shoe_types(shoetype)






