class BudgetTracker:
    def __init__(self):
        self.budget_data = {'income': [], 'expenses': []}

    def add_transaction(self, category, amount, transaction_type):
        transaction = {'category': category, 'amount': amount}
        self.budget_data[transaction_type].append(transaction)

    def display_budget_summary(self):
        print("\nBudget Summary:")
        print("Income:")
        self.display_transactions('income')
        print("\nExpenses:")
        self.display_transactions('expenses')
        print("\nTotal Balance: ${}".format(self.calculate_balance()))

    def display_transactions(self, transaction_type):
        for transaction in self.budget_data[transaction_type]:
            print("- {}: ${}".format(transaction['category'], transaction['amount']))

    def calculate_balance(self):
        total_income = sum(transaction['amount'] for transaction in self.budget_data['income'])
        total_expenses = sum(transaction['amount'] for transaction in self.budget_data['expenses'])
        return total_income - total_expenses

def main():
    tracker = BudgetTracker()

    while True:
        print("\nOptions:")
        print("1. Add Income")
        print("2. Add Expense")
        print("3. Display Budget Summary")
        print("4. Display Income Transactions")
        print("5. Display Expense Transactions")
        print("6. Display Balance")
        print("7. Exit")

        choice = input("Enter your choice (1-7): ")

        if choice == '1':
            category = input("Enter income category: ")
            amount = float(input("Enter amount: "))
            tracker.add_transaction(category, amount, 'income')
        elif choice == '2':
            category = input("Enter expense category: ")
            amount = float(input("Enter amount: "))
            tracker.add_transaction(category, amount, 'expenses')
        elif choice == '3':
            tracker.display_budget_summary()
        elif choice == '4':
            tracker.display_transactions('income')
        elif choice == '5':
            tracker.display_transactions('expenses')
        elif choice == '6':
            print("Total Balance: ${}".format(tracker.calculate_balance()))
        elif choice == '7':
            print("Exiting the Budget Tracker. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 7.")

if __name__ == "__main__":
    main()
