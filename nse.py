from nsetools import Nse
import time
nse = Nse()
q = nse.get_quote('infy')
input_string = input("Enter a list of stocks separated by space : ")
print("\n")
stocknames = input_string.split()
print("Stock list is", stocknames)

def func(stocknames):
    for stock in stocknames:
        q = nse.get_quote(stock)
        #time.sleep(4)
        if q:
            
            CompanyName = q["companyName"]
            Open = q["open"]
            DayHigh = q["dayHigh"]
            DayLow = q["dayLow"]
            ClosePrice = q["closePrice"]
            Volume = q["totalTradedVolume"]
            DeliveryQuantity = q["deliveryQuantity"]
            DeliveryPercentage = q["deliveryToTradedQuantity"]
            print("Company_Name--", CompanyName)
            print("Open--", Open)
            print("Day_High--", DayHigh)
            print("Day_Low--", DayLow)
            print("Close_Price--", ClosePrice)
            print("Volume--", Volume)
            print("DeliveryQuantity--", DeliveryQuantity)
            print("DeliveryPercentage--", DeliveryPercentage)
            print("\n")

func(stocknames)
