# pcost.py

import report
import sys

def portfolio_cost(filename):
    '''
    Computes the total cost (shares*price) of a portfolio file
    '''
    portfolio = report.read_portfolio(filename)
    return sum([s['shares']*s['price'] for s in portfolio])

def main(argv):
	cost = portfolio_cost(argv)
	print('Total cost:', cost)
	
if __name__ == "__main__":
	if len(sys.argv) != 2:
		raise SystemExit(f"Use {sys.argv[0]} ""portfoliofile")
	main(sys.argv[1])


