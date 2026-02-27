# pcost.py
#
# Exercise 1.27
import csv
import sys

def portfolio_cost(filename):
    totalcost = 0.0

    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        for n, row in enumerate(rows):
            try:
                totalcost += int(row[1]) * float(row[2])
            except:
                print(f"Row{n}: multiplication failure: {row}")
    return totalcost

if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'Data/portfolio.csv'

cost = portfolio_cost(filename)
print('Total cost:', cost)
