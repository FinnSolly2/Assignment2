def main():
    # Initialize all managers
    inventory = InventoryManager()
    stock_manager = StockManager(inventory)
    category_manager = CategoryManager(inventory)
    reporting = ReportingSystem(inventory)

    # Add some products
    inventory.add_product(1, "Laptop", 10)
    inventory.add_product(2, "Mouse", 20)
    inventory.add_product(3, "Keyboard", 15)

    # Set up categories
    category_manager.add_category("Electronics", "Electronic devices and accessories")
    category_manager.assign_product_to_category(1, "Electronics")
    category_manager.assign_product_to_category(2, "Electronics")
    category_manager.assign_product_to_category(3, "Electronics")

    # Perform some stock operations
    stock_manager.add_stock(1, 5)
    stock_manager.remove_stock(2, 3)

    # Generate report
    print("Stock Report:")
    for item in reporting.generate_stock_report():
        print(f"Product: {item['name']}, Stock: {item['current_stock']}")

if _name_ == "_main_":
    main()
