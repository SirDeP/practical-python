# pcost.py
#
# Exercise 1.27
def portfolio_cost(filename):
    totalcost = 0.0

    with open(filename, 'rt') as f:
        headers = next(f)
        for line in f:
            row = line.split(',')
            try:
                totalcost += int(row[1]) * float(row[2])
            except:
                print("multiplication failure")
    return totalcost
