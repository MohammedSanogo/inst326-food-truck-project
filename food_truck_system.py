#Mohammed Sanogo,Rachid cisse, Joshuel Robinson and Aby

"""
food_truck_system.py

Simulates a food truck ordering system where users can view a menu, place orders,
and receive receipts. This file contains the core class definitions and structure
for the final project.

Part of INST326 Final Project - Check-in 1
"""

class MenuItem:
    """Represents a single menu item available for purchase."""
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __repr__(self):
        return f"{self.name} - ${self.price:.2f}"


class Order:
    """Handles customer orders with selected items and total price."""
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def calculate_total(self):
        return sum(item.price for item in self.items)

    def generate_receipt(self):
        receipt = "\n".join([str(item) for item in self.items])
        receipt += f"\nTotal: ${self.calculate_total():.2f}"
        return receipt


class Inventory:
    """Tracks available inventory items and stock levels."""
    def __init__(self):
        self.stock = {}

    def update_stock(self, item_name, quantity):
        self.stock[item_name] = self.stock.get(item_name, 0) + quantity

    def is_in_stock(self, item_name):
        return self.stock.get(item_name, 0) > 0


if __name__ == "__main__":
    pass  # Execution entry point for running the food truck system
