import csv

colours = ['red', 'blue', 'green', 'yellow']
print(colours)


'''
colours = ['red', 'blue', 'green', 'yellow']
colour_count = 0
with open('tutorial.csv', 'w', newline = '') as csvfile:
    fieldnames = ['number', 'colour']
    thewriter = csv.DictWriter(csvfile, fieldnames= fieldnames)
    thewriter.writeheader()
    for colour in colours:
        colour_count +=1
        thewriter.writerow({'number':colour_count, 'colour':colour})
'''
#backtest('macd', df, fast_period=12, slow_period=26, signal_period=9, sma_period=30, dir_period=10)

# Starting Portfolio Value: 100000.00
# Final Portfolio Value: 96229.58