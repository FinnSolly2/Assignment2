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
