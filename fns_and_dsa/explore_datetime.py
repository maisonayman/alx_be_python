from datetime import datetime, timedelta

def display_current_datetime():
    current_date = datetime.now()
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print(f"Current date and time: {formatted_date}")
    return current_date  # In case we need it in the next part

def calculate_future_date(current_date, days_to_add):
    future_date = current_date + timedelta(days=days_to_add)
    formatted_future = future_date.strftime("%Y-%m-%d")
    print(f"Future date: {formatted_future}")

def main():
    current_date = display_current_datetime()

    try:
        days = int(input("Enter the number of days to add to the current date: "))
        calculate_future_date(current_date, days)
    except ValueError:
        print("Please enter a valid integer.")

if __name__ == "__main__":
    main()
