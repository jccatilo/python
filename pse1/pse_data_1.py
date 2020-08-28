from fastquant import get_pse_data
from google.colab import files
#from fastquant import backtest
#import csv


stock_name = input("Input stock name(ex. JFC): ")
start_date = input("Input start date(YYYY-MM-DD): ")
end_date = input("Input end date(YYYY-MM-DD): ")

df = get_pse_data(stock_name, start_date, end_date)
df.to_csv('jfc.csv', index=False)

files.download('jfc.csv')
print(df)
print("*****************")
print("nothing follows.")