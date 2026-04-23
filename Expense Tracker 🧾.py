# Expense Tracker 🧾
expenses=[]
budget=float(input("Enter your daily budget:"))
total=0
while True:
    category=input("Enter the category of your expense (e.g. food, transportation, entertainment) or 'done' to finish:")
    if category.lower()=='done':
        break
    amount=float(input("Enter the amount spent:"))
    expenses.append((category, amount))
    total+=amount
print("----Expense Summary----")
for category, amount in expenses:
    print(f"{category} : ${amount}")
print("--------------------------")
print(f"Total expenses: ${total}")
remaining_budget=budget-total
print(f"Remaining budget: ${remaining_budget}")