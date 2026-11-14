
from datetime import date
import math


def split_code(code):
    if not isinstance(code, str):
        return None

    parts = code.strip().upper().split('-')

    if len(parts) != 2:
        return None

    prefix, value = parts

    if not prefix or not value:
        return None

    try:
        number = int(value)
    except ValueError:
        return None

    return prefix, number


def most_expensive(prices_csv):
    if not isinstance(prices_csv, str) or not prices_csv.strip():
        return None

    try:
        prices = [float(p.strip()) for p in prices_csv.split(',')]

        if not prices or not all(math.isfinite(p) for p in prices):
            return None

    except ValueError:
        return None

    return max(prices)


def expiry_days(date_text):
    if not isinstance(date_text, str):
        return None

    try:
        year, month, day = map(int, date_text.split('-'))

        # Reject invalid calendar dates.
        date(year, month, day)

        return (year - 2024) * 365 + (month - 1) * 30 + day

    except (ValueError, TypeError):
        return None


def main():
    print("==== Running split_code ====")
    user_input = input("Enter a coupon code (e.g. save-20): ")
    print("Prefix and Value:", split_code(user_input))

    print("\n==== Running most_expensive ====")
    user_input = input("Enter item prices as CSV (e.g. 199,49.5,320): ")
    print("Most Expensive Item:", most_expensive(user_input))

    print("\n==== Running expiry_days ====")
    user_input = input("Enter an expiry date as YYYY-MM-DD: ")
    print("Days Since 2024:", expiry_days(user_input))


if __name__ == "__main__":
    main()
