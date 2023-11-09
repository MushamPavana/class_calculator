class ShoppingCalculator:
    def __init__(self):
        self.total_expenses = 0

    def add_expense(self, item, cost):
        self.total_expenses += cost
        print(f"Added {item} to the shopping list. Cost: {cost:.2f}")

shopping_calculator = ShoppingCalculator()

shopping_calculator.add_expense("Groceries",3500)
shopping_calculator.add_expense("Clothing", 5000)
shopping_calculator.add_expense("Electronics",21000)

print("\nTotal Expenses: {:.2f}".format(shopping_calculator.total_expenses))
