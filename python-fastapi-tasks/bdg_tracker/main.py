from transaction import Transaction
from budget_utils import save_transactions, load_transactions, group_by_category


def add_expense(transactions):
    category = input("Enter expense category: ")
    try:
        amount = float(input("Enter amount: "))
        if amount <= 0:
            raise ValueError
        new_transaction = Transaction(category, amount)
        transactions.append(new_transaction)
        print("Expense added.")
    except ValueError:
        print("Invalid amount. Please enter a positive number.")

def view_all_expenses(transactions):
    if not transactions:
        print("No expenses recorded.")
        return
    for t in transactions:
        print(t)

def view_category_totals(transactions):
    if not transactions:
        print("No expenses recorded.")
        return
    
    totals = group_by_category(transactions)
    print("\n--- Totals by Category ---")
    for category, total in totals.items():
        print(f"{category}: ₦{total:.2f}")

def main():
    transactions = load_transactions()

    while True:
        print("\nPersonal Budget Tracker")
        print(".......................")
        print("\n1. Add expense")
        print("2. View all expenses")
        print("3. View totals by category")
        print("4. Save & Exit")
        choice = input("\nEnter your choice: ")

        if choice == '1':
            add_expense(transactions)
        elif choice == '2':
            view_all_expenses(transactions)
        elif choice == '3':
            view_category_totals(transactions)
        elif choice == '4':
            save_transactions(transactions)
            print("\nExiting.")
            break
        else:
            print("\nInvalid choice. Please try again.")

if __name__ == "__main__":
    main()