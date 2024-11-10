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
