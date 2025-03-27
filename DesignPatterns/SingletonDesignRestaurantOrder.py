class OrderManager:
    _instance = None  # Stores the single instance

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.orders = []  # List to store orders
        return cls._instance

    def add_order(self, order):
        self.orders.append(order)
        print(f"Order added: {order}")

    def get_orders(self):
        return self.orders


# Usage
restaurant1 = OrderManager()
restaurant2 = OrderManager()

# Adding orders using different instances (should be the same instance)
restaurant1.add_order("Paneer Butter Masala")
restaurant2.add_order("Veg Biryani")

# Checking if both instances refer to the same object
print(restaurant1 is restaurant2)  # True

# Fetching orders from either instance
print(restaurant1.get_orders())  # ['Paneer Butter Masala', 'Veg Biryani']
print(restaurant2.get_orders())  # ['Paneer Butter Masala', 'Veg Biryani']
