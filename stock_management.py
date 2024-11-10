class StockManager:
    def _init_(self, inventory_manager):
        self.inventory = inventory_manager

    def add_stock(self, product_id, quantity):
        product = self.inventory.get_product(product_id)
        if product:
            product.quantity += quantity
            return True
        return False

    def remove_stock(self, product_id, quantity):
        product = self.inventory.get_product(product_id)
        if product and product.quantity >= quantity:
            product.quantity -= quantity
            return True
        return False

    def get_stock_level(self, product_id):
        product = self.inventory.get_product(product_id)
        return product.quantity if product else 0
