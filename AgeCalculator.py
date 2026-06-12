from datetime import datetime

def calculate_age(birth_year):
    current_year = datetime.now().year
    return current_year - birth_year

try:
    birth_year = int(input("Enter your birth year: "))
    current_year = datetime.now().year

    if birth_year < 1900 or birth_year > current_year:
        print("Invalid birth year! Please enter a valid year.")
    else:
        age = calculate_age(birth_year)
        print("Your age is:", age, "years")

except ValueError:
    print("Invalid input! Please enter a numeric year.")