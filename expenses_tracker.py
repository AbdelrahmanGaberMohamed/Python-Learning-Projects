print("Welcome to the Daily Expense Tracker!\n")
menu = ["Menu:", "1. Add a new expense", "2. View all expenses", "3. Calculate total and average expense", "4. Clear all expenses", "5. Exit"]
expenses_lst = []
total = 0 
average = 0
for item in menu:
    print(item)
def expenses_recorded(expenses_lst):
    if len(expenses_lst) == 0:
        return True
    else:
        return False
while True:
    user_input = input()
    match user_input:
        case '1':
            expense = float(input())
            expenses_lst.append(expense)
            print("Expense added successfully!")
        case '2':
            if expenses_recorded(expenses_lst):
                print("No expenses recorded yet.")
                continue
            else:
                print("Your expenses:")
                for index, expense in enumerate(expenses_lst):
                    print(f"{index+1}. {expense}")
        case '3':
            if expenses_recorded(expenses_lst):
                print("No expenses recorded yet.")
                continue
            else:
                for expense in expenses_lst:
                    total += expense
                average = total / len(expenses_lst)
                print(f"Total expense: {total}")
                print(f"Average expense: {average}")
        case '4':
            expenses_lst = []
            print("All expenses cleared.")
        case '5':
            print("Exiting the Daily Expense Tracker. Goodbye!")
            break
        case _:
            print("Invalid choice. Please try again.")
            continue