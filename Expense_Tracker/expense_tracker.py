import uuid 
from datetime import datetime, timezone

class Expense:
    def __init__(self, title, amount):
        """
        Initialize Expense attributes.
        """
        self.id = str(uuid.uuid4())
        self.title = title
        self.amount = amount
        self.created_at = datetime.utcnow()
        self.updated_at = self.created_at

    def update(self, title = None, amount = None):
        """
        This method update expense details.
        """
        if title is not None:
            self.title = title
        if amount is not None:
            self.amount = amount
        self.updated_at = datetime.utcnow()

    def to_dict(self):
        """
        This method returns dictionary representation of the Expense instance.
        """
        return {
        "id": self.id,
        "title": self.title,
        "amount": self.amount,
        "created_at": self.created_at.isoformat(),
        "updated_at": self.updated_at.isoformat()
        }
        


    
class ExpenseDatabase:
    def __init__(self):
        """
        Initialize the ExpenseDatabase instance.
        """
        self.expenses = []

    def add_expense(self, expense):
        """
        This method adds an Expense to the database.
        """
        self.expenses.append(expense)

    def remove_expense(self, expense_id):
        """
        This method remove an Expense from the database.
        """
        self.expenses = [exp for exp in self.expenses if exp.id != expense_id]

    def get_expense_by_id(self, expense_id):
        """
        This method gets an Expense by ID.
        """
        for exp in self.expenses:
            if exp.id == expense_id:
                return exp
        return None
    
    def get_expense_by_title(self, title):
        """
        This method gets Expenses by title.
        """
        return [expense for expense in self.expenses if expense.title == title]

    def to_dict(self):
        """
        This method returns a list of dictionaries representing expenses in the database.
        """
        return [expense.to_dict() for expense in self.expenses]