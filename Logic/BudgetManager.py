from Projects.BudgetBuddy.Logic.models.IncomeEntry import IncomeEntry
from Projects.BudgetBuddy.Logic.models.ExpenseEntry import ExpenseEntry
from Projects.BudgetBuddy.Logic.models.Entry import Entry

class BudgetManager:



    def __init__(self):
        self.income = []
        self.expense = []

    def add_income(self, income:IncomeEntry):
        self.income.append(income)

    def add_expense(self, expense:ExpenseEntry):
        self.expense.append(expense)

    def get_total_income(self):
        total = 0
        for value in self.income:
            total += value.get_amount()
        return total

    def get_total_expense(self):
         total = 0
         for value in self.expense:
             total += value.get_amount()
         return total

    def get_net_total(self):
        return self.get_total_income() - self.get_total_expense()
