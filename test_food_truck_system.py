import unittest
from food_truck_system import MenuItem, Order, Inventory

class TestMenuItem(unittest.TestCase):
    def test_repr(self):
        item = MenuItem("Burger", 5.99)
        self.assertEqual(repr(item), "Burger - $5.99")


class TestOrder(unittest.TestCase):
    def test_add_item_and_total(self):
        order = Order()
        item1 = MenuItem("Fries", 2.50)
        item2 = MenuItem("Drink", 1.50)
        order.add_item(item1)
        order.add_item(item2)
        self.assertEqual(order.calculate_total(), 4.00)

    def test_generate_receipt(self):
        order = Order()
        order.add_item(MenuItem("Taco", 3.00))
        receipt = order.generate_receipt()
        self.assertIn("Taco", receipt)
        self.assertIn("Total: $3.00", receipt)


class TestInventory(unittest.TestCase):
    def test_stock_update_and_check(self):
        inventory = Inventory()
        inventory.update_stock("Burger", 5)
        self.assertTrue(inventory.is_in_stock("Burger"))
        self.assertFalse(inventory.is_in_stock("Soda"))


if __name__ == '__main__':
    unittest.main()
