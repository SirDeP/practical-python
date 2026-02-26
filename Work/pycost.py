def portfolio_cost(filename):
    f = open(filename, 'rt')
    amount = 0
    price = 0
    cost = 0.0
    total_cost = 0
    headers = next(f).split(',')
    for line in f:
        row = line.split(',')
        amount = int(row[1])
        price = float(row[2])
        # print (amount, price)
        cost = amount * price
        total_cost += cost
    return total_cost
    # print("Total Cost: ", total_cost)