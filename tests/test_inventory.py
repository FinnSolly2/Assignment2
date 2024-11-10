import unittest
from datetime import datetime

# Import our modules
from basic_inventory import Product, InventoryManager

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

class TestIntegration(unittest.TestCase):
    def setUp(self):
        self.inventory = InventoryManager()
        self.stock_manager = StockManager(self.inventory)
        self.category_manager = CategoryManager(self.inventory)
        self.reporting = ReportingSystem(self.inventory)

    def test_complete_workflow(self):
        """Test complete system workflow"""
        # 1. Add products
        self.inventory.add_product(1, "Laptop", 0)
        self.inventory.add_product(2, "Mouse", 0)

        # 2. Create category and assign products
        self.category_manager.add_category("Electronics")
        self.category_manager.assign_product_to_category(1, "Electronics")
        self.category_manager.assign_product_to_category(2, "Electronics")

        # 3. Perform stock operations
        self.stock_manager.add_stock(1, 10)
        self.stock_manager.add_stock(2, 20)
        self.stock_manager.remove_stock(1, 3)

        # 4. Log transactions
        self.reporting.log_transaction(1, 10, "ADD")
        self.reporting.log_transaction(2, 20, "ADD")
        self.reporting.log_transaction(1, 3, "REMOVE")

        # 5. Verify final state
        report = self.reporting.generate_stock_report()
        self.assertEqual(len(report), 2)
        
        laptop_report = next(r for r in report if r['id'] == 1)
        self.assertEqual(laptop_report['current_stock'], 7)
        self.assertEqual(laptop_report['transactions'], 2)
        
        mouse_report = next(r for r in report if r['id'] == 2)
        self.assertEqual(mouse_report['current_stock'], 20)
        self.assertEqual(mouse_report['transactions'], 1)
        
        # 6. Verify categories
        electronics_products = self.category_manager.get_products_in_category("Electronics")
        self.assertEqual(len(electronics_products), 2)
        self.assertEqual({p.id for p in electronics_products}, {1, 2})
