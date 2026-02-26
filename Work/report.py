# report.py
#
# Exercise 2.4
import csv

def read_portfolio(filename):
    portfolio = []
    # d = {}
    with open(filename, 'rt') as f:
        # headers = next(f).split(',')
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            # holding = (row[0], int(row[1]), float(row[2]))
            # portfolio.append(holding)
            # d['name'] = row[0]
            # d['shares'] = int(row[1])
            # d['price'] = float(row[2])
            d = { 'name' : row[0], 'shares' : int(row[1]), 'price' : float(row[2])}
            portfolio.append(d)
    return portfolio

def read_prices(filename):
    pricelist = {}
    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        for row in rows:
            # print(row[0])
            
            if row:
                pricelist[row[0]] = float(row[1])
            else:
                pass
    return pricelist

def gain_loss(f_portfolio, f_pricelist):
    portfolio = read_portfolio(f_portfolio)
    pricelist = read_prices(f_pricelist)

    for i in range(len(portfolio)):
        stock = portfolio[i]['name']
        stock_amount = portfolio[i]['shares']
        boughtprice = float(portfolio[i]['price'])
        sellprice = pricelist[stock]
        print(stock, boughtprice, sellprice)