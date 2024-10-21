# Exercise 5: Days of the Month - 30 Marks

daysofthemonth = {
    1: 31,   # January
    2: 28,   # February (default)
    3: 31,   # March
    4: 30,   # April
    5: 31,   # May
    6: 30,   # June
    7: 31,   # July
    8: 31,   # August
    9: 30,   # September
    10: 31,  # October
    11: 30,  # November
    12: 31   # December
}

def main():
    month = int(input("Enter the number of a month")) # I make a variable and ask the user to input a number of the month.
    
    if 1 <= month <= 12:
        if month == 2: # Adjust my code to cater for the leap year
            leap_year = input("Is it a leap year? (yes/no)").strip().lower() # Check if its a leap year or not.
            if leap_year == 'yes': 
                print("Febuary has 29 days.") # Print the first outcome.
            else:
                print("Febuary has 28 days.") # Print the second outcome.
        else:
            days = daysofthemonth[month] # Use month as the key. use days as the value/result.
            print(f"There are {days} days in {month}") # Print the days in the chosen month.
    else:
        print("Invalid number.") # Error message if the bounders dont fit " 1 <= month <= 12: "

main() # Finally, call the function.