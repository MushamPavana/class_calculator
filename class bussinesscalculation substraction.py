class BusinessCalculator:
    def subtract(self, revenue, total_expenses):
        return revenue - total_expenses

calculator = BusinessCalculator()

expenses = [2000, 1000, 8000]
total_expenses = sum(expenses)

remaining_budget = calculator.subtract(5000, total_expenses)

revenue = 8000
expenses = 11000

loss = calculator.subtract(revenue, expenses)

print(f"Total Expenses: {total_expenses}")
print(f"Remaining Budget: {remaining_budget}")
print(f"Loss: {loss}")
