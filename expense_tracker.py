import json
import datetime
FILE_NAME = "expenses.json"

# Load expenses from file
def load_expenses():
    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

# Save expenses to file
def save_expenses(expenses):
    with open(FILE_NAME, "w") as file:
        json.dump(expenses, file, indent=4)

# Add a new expense
def add_expense(expenses):
    amount = float(input("Enter amount: "))
    category = input("Enter category (e.g., Food, Transport): ")
    date = input("Enter date (YYYY-MM-DD) or leave blank for today: ")
    if not date:
        date = str(datetime.date.today())
    expenses.append({
        "amount": amount,
        "category": category,
        "date": date
    })
    save_expenses(expenses)
    print("Expense added successfully!")
# View summary
def view_summary(expenses):
    print("\n1. Total spending by category")
    print("2. Total overall spending")
    print("3. Spending over time (by date)")
    choice = input("Select an option: ")
    if choice == "1":
        category_totals = {}
        for e in expenses:
            category_totals[e["category"]] = category_totals.get(e["category"], 0) + e["amount"]
        for cat, total in category_totals.items():
            print(f"{cat}: ${total:.2f}")
    elif choice == "2":
        total = sum(e["amount"] for e in expenses)
        print(f"Total spending: ${total:.2f}")
    elif choice == "3":
        date_totals = {}
        for e in expenses:
            date_totals[e["date"]] = date_totals.get(e["date"], 0) + e["amount"]
        for d, total in sorted(date_totals.items()):
            print(f"{d}: ${total:.2f}")
    else:
        print("Invalid choice.")

# Main menu
def main():
    expenses = load_expenses()
    while True:
        print("\n--- Personal Expense Tracker ---")
        print("1. Add expense")
        print("2. View summary")
        print("3. Exit")
        choice = input("Choose an option: ")
        if choice == "1":
            add_expense(expenses)
        elif choice == "2":
            view_summary(expenses)
        elif choice == "3":
            break
        else:
            print("Invalid choice.")
if __name__ == "__main__":
    main()
