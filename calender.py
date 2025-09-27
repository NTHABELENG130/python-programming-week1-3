import calendar

def display_month_calendar():
    try:
        year = int(input("Enter the year (e.g., 2025): "))
        month = int(input("Enter the month (1-12): "))

        if not (1 <= month <= 12):
            print("Invalid month! Please enter a number between 1 and 12.")
            return

        print(calendar.month(year, month))
    except ValueError:
        print("Invalid input! Please enter numeric values for year and month.")

display_month_calendar()