import unittest
from datetime import datetime

# Import our modules
from basic_inventory import Product, InventoryManager
from stock_management import StockManager
from product_categories import CategoryManager, Category
from reporting import ReportingSystem, Transaction

class TestProduct(unittest.TestCase):
    def setUp(self):
        self.product = Product(1, "Test Product", 10)

    def test_product_initialization(self):
        """Test basic product creation and attributes"""
        self.assertEqual(self.product.id, 1)
        self.assertEqual(self.product.name, "Test Product")
        self.assertEqual(self.product.quantity, 10)

class TestInventoryManager(unittest.TestCase):
    def setUp(self):
        self.inventory = InventoryManager()

    def test_add_product(self):
        """Test adding products to inventory"""
        # Test new product addition
        self.assertTrue(self.inventory.add_product(1, "Laptop", 5))
        
        # Test duplicate product
        self.assertFalse(self.inventory.add_product(1, "Laptop", 5))
        
        # Verify product details
        product = self.inventory.get_product(1)
        self.assertEqual(product.name, "Laptop")
        self.assertEqual(product.quantity, 5)

    def test_get_nonexistent_product(self):
        """Test retrieving non-existent product"""
        self.assertIsNone(self.inventory.get_product(999))

class TestStockManager(unittest.TestCase):
    def setUp(self):
        self.inventory = InventoryManager()
        self.stock_manager = StockManager(self.inventory)
        self.inventory.add_product(1, "Test Product", 10)

    def test_add_stock(self):
        """Test adding stock to existing product"""
        self.assertTrue(self.stock_manager.add_stock(1, 5))
        self.assertEqual(self.stock_manager.get_stock_level(1), 15)

    def test_remove_stock(self):
        """Test removing stock from existing product"""
        self.assertTrue(self.stock_manager.remove_stock(1, 5))
        self.assertEqual(self.stock_manager.get_stock_level(1), 5)

    def test_get_stock_level(self):
        """Test stock level retrieval"""
        self.assertEqual(self.stock_manager.get_stock_level(1), 10)
        self.assertEqual(self.stock_manager.get_stock_level(999), 0)

class TestCategoryManager(unittest.TestCase):
    def setUp(self):
        self.inventory = InventoryManager()
        self.category_manager = CategoryManager(self.inventory)
        self.inventory.add_product(1, "Laptop", 5)
        self.inventory.add_product(2, "Mouse", 10)

    def test_add_category(self):
        """Test category creation"""
        self.assertTrue(self.category_manager.add_category("Electronics", "Electronic devices"))
        self.assertFalse(self.category_manager.add_category("Electronics", "Duplicate category"))

    def test_assign_product_to_category(self):
        """Test product assignment to categories"""
        self.category_manager.add_category("Electronics")
        self.assertTrue(self.category_manager.assign_product_to_category(1, "Electronics"))
        self.assertFalse(self.category_manager.assign_product_to_category(999, "Electronics"))
        self.assertFalse(self.category_manager.assign_product_to_category(1, "NonExistent"))

    def test_get_products_in_category(self):
        """Test retrieving products in a category"""
        self.category_manager.add_category("Electronics")
        self.category_manager.assign_product_to_category(1, "Electronics")
        self.category_manager.assign_product_to_category(2, "Electronics")
        
        products = self.category_manager.get_products_in_category("Electronics")
        self.assertEqual(len(products), 2)
        self.assertEqual({p.id for p in products}, {1, 2})

class TestStockValidation(unittest.TestCase):
    def setUp(self):
        self.inventory = InventoryManager()
        self.stock_manager = StockManager(self.inventory)
        self.inventory.add_product(1, "Test Product", 10)

    def test_negative_quantities(self):
        """Test validation against negative quantities"""
        self.assertFalse(self.stock_manager.add_stock(1, -5))
        self.assertFalse(self.stock_manager.remove_stock(1, -5))
        self.assertEqual(self.stock_manager.get_stock_level(1), 10)

    def test_excessive_removal(self):
        """Test validation against removing more than available"""
        self.assertFalse(self.stock_manager.remove_stock(1, 15))
        self.assertEqual(self.stock_manager.get_stock_level(1), 10)

from datetime import datetime

class Transaction:
    def _init_(self, product_id, quantity, transaction_type):
        self.product_id = product_id
        self.quantity = quantity
        self.type = transaction_type
        self.timestamp = datetime.now()

class ReportingSystem:
    def _init_(self, inventory_manager):
        self.inventory = inventory_manager
        self.transactions = []

    def log_transaction(self, product_id, quantity, transaction_type):
        self.transactions.append(
            Transaction(product_id, quantity, transaction_type)
        )

    def get_product_history(self, product_id):
        return [t for t in self.transactions if t.product_id == product_id]

    def generate_stock_report(self):
        report = []
        for product_id, product in self.inventory.products.items():
            report.append({
                'id': product_id,
                'name': product.name,
                'current_stock': product.quantity,
                'transactions': len(self.get_product_history(product_id))
            })
        return report

