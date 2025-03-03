
import datetime
import calendar

from datetime import date

check = open('check.txt', 'w+')
log = open('log.txt', 'a+')

#today = date.today()

today = '2025-03-03'

def check_weekday_or_weekend(date):
    try:
        # Convert the input date string to a datetime object
        given_date = datetime.datetime.strptime(date, '%Y-%m-%d')

        # Use isoweekday() to get the weekday (Monday is 1 and Sunday is 7)
        day_of_week = (given_date.weekday() + 1) % 7  # Convert Sunday from 6 to 0

        # Determine if it's a weekday or a weekend
        if 0 < day_of_week < 6:
            day_type = 'weekday'
        else:
            day_type = 'weekend'

        # Print the result
        #return day_of_week
        #check.write(f"{day_of_week}\n")
        check.write(f"{day_type}")
        log.write(f"{today}\n")
        #print(f"The day of the week for {given_date.strftime('%Y-%m-%d')} is {day_of_week} ({day_type})")

    except ValueError as e:
        print(f"Error: {e}")

# Example usage
date = str(today)
check_weekday_or_weekend(date)



