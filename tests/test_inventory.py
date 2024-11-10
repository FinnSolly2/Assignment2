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
