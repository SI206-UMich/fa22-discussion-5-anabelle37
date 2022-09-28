import unittest

# Counts the number of a's in a sentence (e.g., a string)
def count_a(sentence):
	total = 0
	for i in range(len(sentence) - 1):
		if sentence[i] == 'a' or sentence[i] == "A":
			total += 1
	return total


# Item class
# Describes an item to be sold. Each item has a name, a price, and a stock.
class Item:
	# Constructor.
	def __init__(self, name, price, stock):
		self.name = name
		self.price = price
		self.stock = stock

	# Print
	def __str__(self):
		return ("Item = {}, Price = {}, Stock = {}".format(self.name, self.price, self.stock))

# Warehouse class
# A warehouse stores items and manages them accordingly.
class Warehouse:

	# Constructor
	def __init__(self, items = []):
		self.items = items[:]

	# Prints all the items in the warehouse, one on each line.	
	def print_items(self):
		for item in self.items:
			print(item)
			print("\n")	

	# Adds an item to the warehouse	
	def add_item(self, item):
		self.items.append(item)

	# Returns the item in the warehouse with the most stock		
	def get_max_stock(self):
		stock=0
		for item in self.items:
			if item.stock > stock:
				stock= item.stock
		return stock

	
	# Returns the item in the warehouse with the highest price
	def get_max_price(self):
		maxVal=0
		for item in self.items:
			if item.price > maxVal:
				maxVal=item.price
		return maxVal	



# Tests
class TestAllMethods(unittest.TestCase):

	# SetUp -- we create a bunch of items for you to use in your tests.
	def setUp(self):
		self.item1 = Item("Beer", 6, 20)
		self.item2 = Item("Cider", 5, 25)
		self.item3 = Item("Water", 1, 100)
		self.item4 = Item("Fanta", 2, 60)
		self.item5 = Item("CocaCola", 3, 40)

	## Check to see whether count_a works
	def test_count_a(self):
		self.assertEqual(count_a("Anabelle"), 2)


	## Check to see whether you can add an item to the warehouse
	def test_add_item(self): 
		w1=Warehouse()
		self.assertEqual(len(w1.items),0)
		w1.add_item(self.item1)
		self.assertEqual(len(w1.items),1)

	## Check to see whether warehouse correctly returns the item with the most stock
	def test_warehouse_max_stocks(self):
		w2=Warehouse()
		w2.add_item(self.item1)
		w2.add_item(self.item3)
		self.assertEqual(w2.get_max_stock(), self.item3.stock)

	# Check to see whether the warehouse correctly return the item with the highest price
	def test_warehouse_max_price(self):
		w3=Warehouse()
		w3.add_item(self.item1)
		w3.add_item(self.item3)
		self.assertEqual(w3.get_max_price(), self.item1.price)
		

def main():
	unittest.main()

if __name__ == "__main__":
	main()