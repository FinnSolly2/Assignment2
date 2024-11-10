class Category:
    def __init__(self, name, description=""):
        self.name = name
        self.description = description
        self.products = set()

class CategoryManager:
    def __init__(self, inventory_manager):
        self.inventory = inventory_manager
        self.categories = {}

    def add_category(self, name, description=""):
        if name not in self.categories:
            self.categories[name] = Category(name, description)
            return True
        return False

    def assign_product_to_category(self, product_id, category_name):
        if category_name in self.categories and product_id in self.inventory.products:
            self.categories[category_name].products.add(product_id)
            return True
        return False

    def get_products_in_category(self, category_name):
        if category_name in self.categories:
            return [self.inventory.get_product(pid) for pid in self.categories[category_name].products]
        return []
