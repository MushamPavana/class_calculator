class GroceryCalculator:
    def __init__(self):
        self.total_cost = 0

    def add_item(self, item_name, price, quantity):
        item_cost = price * quantity
        self.total_cost += item_cost
        print(f"Added {quantity} {item_name} {item_cost:.2f}")

grocery_calculator = GroceryCalculator()

grocery_calculator.add_item("Apple", 10, 3)
grocery_calculator.add_item("Bread", 50, 2)
grocery_calculator.add_item("Milk", 23, 1)

print("\nTotal Cost for all items: {:.2f}".format(grocery_calculator.total_cost))
