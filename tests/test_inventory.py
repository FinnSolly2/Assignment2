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
