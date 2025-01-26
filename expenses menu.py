expenses = []


def show_expenses():
    if not expenses:
        print("No expenses recorded yet.")
    else:
        print("\n--- Expense List ---")
        for idx, expense in enumerate(expenses, start=1):
            print(f"{idx}. {expense['description']} - ${expense['amount']:.2f}")
        print("--------------------")


def add_expense():
    description = input("Enter a description for the expense: ")
    try:
        amount = float(input("Enter the amount of the expense: "))
        expenses.append({"description": description, "amount": amount})
        print(f"Expense '{description}' of ${amount:.2f} added successfully!")
    except ValueError:
        print("Invalid amount. Please enter a numeric value.")


def show_total_expenses():
    total = sum(expense['amount'] for expense in expenses)
    print(f"\nTotal Expenses: ${total:.2f}")


def delete_expense():
    try:
        show_expenses()
        choice = int(input("Enter the number of the expense to delete: ")) - 1
        if 0 <= choice < len(expenses):
            removed_expense = expenses.pop(choice)
            print(f"Expense '{removed_expense['description']}' deleted successfully.")
        else:
            print("Invalid choice. Expense not found.")
    except ValueError:
        print("Please enter a valid number.")
    except IndexError:
        print("Invalid expense number. Please select a valid number.")


def clear_all_expenses():
    global expenses
    expenses = []
    print("All expenses have been cleared.")


def sort_expenses():
    print("\nSort Expenses By:")
    print("1. Description")
    print("2. Amount")
    choice = input("Enter your choice: ")
    if choice == '1':
        expenses.sort(key=lambda x: x['description'].lower())
        print("Expenses sorted by description.")
    elif choice == '2':
        expenses.sort(key=lambda x: x['amount'])
        print("Expenses sorted by amount.")
    else:
        print("Invalid choice. No sorting applied.")


def find_expense():
    description = input("Enter the description of the expense you want to find: ").lower()
    found_expenses = [expense for expense in expenses if description in expense['description'].lower()]
    if found_expenses:
        print("\n--- Found Expenses ---")
        for expense in found_expenses:
            print(f"{expense['description']} - ${expense['amount']:.2f}")
        print("----------------------")
    else:
        print(f"No expenses found with the description '{description}'.")


def update_expense():
    try:
        show_expenses()
        choice = int(input("Enter the number of the expense to update: ")) - 1
        if 0 <= choice < len(expenses):
            new_description = input("Enter new description: ")
            try:
                new_amount = float(input("Enter new amount: "))
                expenses[choice]['description'] = new_description
                expenses[choice]['amount'] = new_amount
                print("Expense updated successfully.")
            except ValueError:
                print("Invalid amount. Please enter a numeric value.")
        else:
            print("Invalid choice. Expense not found.")
    except ValueError:
        print("Please enter a valid number.")


def show_menu():
    print("\n--- Expense Tracker Menu ---")
    print("hello!Shakhawatul,welcome my house")
    print("1. Add a New Expense")
    print("2. View All Expenses")
    print("3. Show Total Expenses")
    print("4. Delete Expense")
    print("5. Clear All Expenses")
    print("6. Sort Expenses")
    print("7. Find Expense by Description")
    print("8. Update Expense")
    print("9. Exit")


def handle_choice(choice):
    if choice == '1':
        add_expense()
    elif choice == '2':
        show_expenses()
    elif choice == '3':
        show_total_expenses()
    elif choice == '4':
        delete_expense()
    elif choice == '5':
        clear_all_expenses()
    elif choice == '6':
        sort_expenses()
    elif choice == '7':
        find_expense()
    elif choice == '8':
        update_expense()
    elif choice == '9':
        print("Exiting the Expense Tracker. Goodbye!")
        return False
    else:
        print("Invalid choice. Please try again.")
    return True


while True:
    show_menu()
    user_choice = input("Enter your choice: ")
    if not handle_choice(user_choice):
        break