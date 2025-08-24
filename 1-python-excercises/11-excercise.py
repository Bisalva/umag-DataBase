

daily_expenses = [100, 320 ,450]
weekly_expenses = [500,600,720]

def calculate_daily_expenses(expenses):
    return sum(expenses) / len(expenses)

def calculate_weekly_expenses():
    return {week: calculate_daily_expenses(weekly_expenses) for week, weekly_expenses in weekly_expenses.items()}



print(int(calculate_daily_expenses(daily_expenses)))
print(int(calculate_daily_expenses(weekly_expenses)))
