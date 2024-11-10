class Product:
	def __init__(self, id, name, quantity=0):
		self.id = id
		self.name = name
		self.quantity = quantity

class InventoryManager:
	def __init__(self):
		self.products = {}

	def add_product(self, id, name, quantity=0):
		if id not in self.products:
			self.products[id] = Product(id, name, quantity)
			return True
		return False

	def get_product(self, id):
		return self.products.get(id)
