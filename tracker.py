#smart expense tracker
import os

FILE_NAME = "expenses.csv"

# -------------------- Utility Functions --------------------

def ensure_file_exists():
    if not os.path.exists(FILE_NAME):
        open(FILE_NAME, "w").close()


def get_valid_amount():
    while True:
        try:
            amount = float(input("Enter amount: "))
            if amount <= 0:
                print(" Amount must be greater than zero.")
            else:
                return amount
        except ValueError:
            print(" Please enter a valid number.")


# -------------------- Core Features --------------------

def add_expense():
    date = input("Enter date (YYYY-MM-DD): ")
    amount = get_valid_amount()
    category = input("Enter category (Food/Travel/etc): ")
    note = input("Enter note: ")

    with open(FILE_NAME, "a") as file:
        file.write(f"{date},{amount},{category},{note}\n")

    print(" Expense added successfully!")


def view_expenses():
    if os.path.getsize(FILE_NAME) == 0:
        print(" No expenses recorded yet.")
        return

    print("\nDate         Amount    Category     Note")
    print("-" * 45)

    with open(FILE_NAME, "r") as file:
        for line in file:
            date, amount, category, note = line.strip().split(",")
            print(f"{date:<12} {amount:<9} {category:<12} {note}")


def total_expense():
    total = 0

    with open(FILE_NAME, "r") as file:
        for line in file:
            total += float(line.split(",")[1])

    print(f"💰 Total Expense: {total}")


def category_summary():
    summary = {}

    with open(FILE_NAME, "r") as file:
        for line in file:
            parts = line.strip().split(",")
            if len(parts) < 4:
                continue

            category = parts[2]
            amount = float(parts[1])

            summary[category] = summary.get(category, 0) + amount

    if not summary:
        print(" No expenses recorded yet.")
        return

    print("\n Category-wise Summary")
    print("-" * 30)
    for category, amount in summary.items():
        print(f"{category:<15} {amount}")


def search_by_category():
    search = input("Enter category to search: ").lower()
    found = False

    with open(FILE_NAME, "r") as file:
        for line in file:
            date, amount, category, note = line.strip().split(",")
            if category.lower() == search:
                if not found:
                    print("\nDate         Amount    Category     Note")
                    print("-" * 45)
                print(f"{date:<12} {amount:<9} {category:<12} {note}")
                found = True

    if not found:
        print(" No expenses found for this category.")


def budget_alert():
    limit = get_valid_amount()
    total = 0

    with open(FILE_NAME, "r") as file:
        for line in file:
            total += float(line.split(",")[1])

    if total > limit:
        print(" Budget exceeded!")
    else:
        print(" You are within your budget.")


# -------------------- Menu --------------------

def show_menu():
    print("\n" + "=" * 40)
    print("        SMART EXPENSE TRACKER")
    print("=" * 40)
    print("1. Add Expense")
    print("2. View All Expenses")
    print("3. View Total Expense")
    print("4. Category-wise Summary")
    print("5. Search by Category")
    print("6. Budget Alert")
    print("7. Exit")


# -------------------- Main Program --------------------

def main():
    ensure_file_exists()

    while True:
        show_menu()
        choice = input("Choose an option (1-7): ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            total_expense()
        elif choice == "4":
            category_summary()
        elif choice == "5":
            search_by_category()
        elif choice == "6":
            budget_alert()
        elif choice == "7":
            print(" Exiting... Thank you for using Expense Tracker!")
            break
        else:
            print(" Invalid choice. Please select 1–7.")


if __name__ == "__main__":
    main()
