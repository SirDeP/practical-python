class Stock:
	def __init__(self,name,shares,price):
		self.name = name
		self.shares = int(shares)
		self.price = float(price)
	
	def cost(self):
		print(self.shares * self.price)
	
	def sell(self, ammount):
		self.shares -= ammount