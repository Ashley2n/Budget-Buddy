from LU2.BudgetBuddy.Logic.models.Entry import Entry

class ExpenseEntry(Entry):

    def __init__(self, description: str = "Unknown Description", amount: float = 0):
        super().__init__(description, amount)

    def get_amount(self):
        return self.amount