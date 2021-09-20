"""
Project for Week 4 of "Python Programming Essentials".
Collection of functions to process dates.

Be sure to read the project description page for further information
about the expected behavior of the program.
"""

import datetime

def days_in_month(year, month):
    """
    Inputs:
      year  - an integer between datetime.MINYEAR and datetime.MAXYEAR
              representing the year
      month - an integer between 1 and 12 representing the month

    Returns:
      The number of days in the input month.
    """
    if 1 <= month <= 11:
        date1 = datetime.date(year, month, 1)
        date2 = datetime.date(year, month + 1, 1)
        return (date2 - date1).days
    elif month == 12:
        date1 = datetime.date(year, month, 1)
        date2 = datetime.date(year + 1, 1, 1)
        return (date2 - date1).days
    else:
        return False

print(days_in_month(2021, 2))

    
def is_valid_date(year, month, day):
    """
    Inputs:
      year  - an integer representing the year
      month - an integer representing the month
      day   - an integer representing the day

    Returns:
      True if year-month-day is a valid date and
      False otherwise
    """
    if year < datetime.MINYEAR or year > datetime.MAXYEAR:
        return False
    elif month <1 or month > 12:
        return False
    elif day < 1 or day > days_in_month(year, month): 
        return False
    else:
        return True

print()

print(is_valid_date(2021, 9, 10))
print(is_valid_date(2021, 9, 33))
print(is_valid_date(2021, 18, 10))
print(is_valid_date(10000, 9, 10))


def days_between(year1, month1, day1, year2, month2, day2):
    """
    Inputs:
      year1  - an integer representing the year of the first date
      month1 - an integer representing the month of the first date
      day1   - an integer representing the day of the first date
      year2  - an integer representing the year of the second date
      month2 - an integer representing the month of the second date
      day2   - an integer representing the day of the second date

    Returns:
      The number of days from the first date to the second date.
      Returns 0 if either date is invalid or the second date is
      before the first date.
    """ 
     
    if is_valid_date(year1, month1, day1) and is_valid_date(year2, month2, day2):
        date1 = datetime.date(year1, month1, day1)
        date2 = datetime.date(year2, month2, day2)
        if date2 > date1:
            number_of_days = date2 - date1
            return number_of_days.days
        else:
            return 0
    else:
        return 0

print()

print(days_between(2020, 18, 4, 2021, 3, 5))
print(days_between(2021, 9, 10, 2020, 9, 10))
print(days_between(2020, 9, 10, 2021, 9, 10))


def age_in_days(year, month, day):
    """
    Inputs:
      year  - an integer representing the birthday year
      month - an integer representing the birthday month
      day   - an integer representing the birthday day

    Returns:
      The age of a person with the input birthday as of today.
      Returns 0 if the input date is invalid or if the input
      date is in the future.
    """
    
    if (is_valid_date(year, month, day)):
        today = datetime.date.today()
        person_bday = datetime.date(year, month, day)
        if (person_bday < today):
            person_age_in_days = days_between(year, month, day, today.year, today.month, today.day)
            return person_age_in_days
        else:
            return 0
    else:
        return 0


print()
    
print(age_in_days(2000, 15, 10))
print(age_in_days(2021, 9, 20))
print(age_in_days(1995, 3, 21))
