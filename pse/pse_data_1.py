from fastquant import get_pse_data
#from fastquant import backtest
#import csv


stock_name = input("Input stock name(ex. JFC): ")
start_date = input("Input start date(YYYY-MM-DD): ")
end_date = input("Input end date(YYYY-MM-DD): ")

df = get_pse_data(stock_name, start_date, end_date)
print(df)
print("*****************")
print("nothing follows.")