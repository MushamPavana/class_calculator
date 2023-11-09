class BusinessCalculator:
    def __init__(self):
        self.total_revenue = 0
        self.total_expenses = 0

    def add_revenue(self, amount):
        self.total_revenue += amount

    def add_expense(self, amount):
        self.total_expenses += amount

    def calculate_profit(self):
        return self.total_revenue - self.total_expenses

    def calculate_profit_margin(self):
        if self.total_revenue != 0:
            return (self.calculate_profit() / self.total_revenue) * 100
        else:
            return "Cannot calculate profit margin, total revenue is zero."

business_calculator = BusinessCalculator()

business_calculator.add_revenue(100000)
business_calculator.add_expense(40000)
business_calculator.add_expense(20000)

profit = business_calculator.calculate_profit()
profit_margin = business_calculator.calculate_profit_margin()

print("Total Revenue: {}".format(business_calculator.total_revenue))
print("Total Expenses: {}".format(business_calculator.total_expenses))
print("Profit: {}".format(profit))
print("Profit Margin: {:.2f}%".format(profit_margin))
