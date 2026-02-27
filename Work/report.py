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
    total_gain_los = 0.0
    for i in range(len(portfolio)):
        stock = portfolio[i]['name']
        stock_amount = portfolio[i]['shares']
        boughtprice = float(portfolio[i]['price'])
        sellprice = pricelist[stock]
        bought_value = stock_amount * boughtprice
        current_value = stock_amount * sellprice
        gain_los = bought_value - current_value
        total_gain_los += gain_los
        print(stock, f'{bought_value:0.2f}', f'{current_value:0.2f}', f'{gain_los:0.2f}')
    print('Total gain loss', f'{total_gain_los}')

def make_report(portfolio, prices):
    report = []
    for i in range(len(portfolio)):
        stockname = portfolio[i]['name']
        gainloss = float(portfolio[i]['price']) - prices[stockname]
        res = (stockname, int(portfolio[i]['shares']), float(prices[ stockname ]), -float(gainloss) ) #float(portfolio[i]['price']) )
        report.append(res)
    return report

report =make_report(read_portfolio('Data/portfolio.csv'), read_prices('Data/prices.csv'))

#for r in report:
#    print( '%10s %10d %10.2f %10.2f' % r )
size = 10
headers = ('Name', 'Shares', 'Price', 'Change')
print ( f'{headers[0]:>{size}s} {headers[1]:>{size}s} {headers[2]:>{size}s} {headers[3]:>{size}s}')
s = ''
for i in range(size):
    s += '-'

print(s, s, s, s)
for name, shares, price, change in report:
    price = '$' + str(price)
    print(f'{name:>10s} {shares:>10d} {price:>10s} {change:>10.2f}')
