"""
Solution to Problem 19 of Project Euler.

You are given the following information, but you may prefer to do some research
for yourself.

1 Jan 1900 was a Monday.
Thirty days has September,
April, June and November.
All the rest have thirty-one,
Saving February alone,
Which has twenty-eight, rain or shine.
And on leap years, twenty-nine.
A leap year occurs on any year evenly divisible by 4, but not on a century
unless it is divisible by 400.
How many Sundays fell on the first of the month during the twentieth century
(1 Jan 1901 to 31 Dec 2000)?
"""


# Dictionary to take days (in word form) into their number representations
DAY_DICT = {
    'Sunday': 1,
    'Monday': 2,
    'Tuesday': 3,
    'Wednesday': 4,
    'Thursday': 5,
    'Friday': 6,
    'Saturday': 7
}


# Dictionary to take months (in number form) into their word representations
MONTH_DICT = {
    1: 'January',
    2: 'February',
    3: 'March',
    4: 'April',
    5: 'May',
    6: 'June',
    7: 'July',
    8: 'August',
    9: 'September',
    10: 'October',
    11: 'November',
    12: 'December'
}


def get_num_days_in_month(month, year):
    """
    Return the number of days in the current month.

    Inputs:
    <month>: <int> a number from 0-11
    <year>: <int> any number
    """
    def is_leap_year():
        """Return True if <year> is a leap year, else return False."""
        if year % 4 == 0:
            if year % 100 == 0:
                if year % 400 == 0:
                    return True
                else:
                    return False
            else:
                return True
        else:
            return False

    if MONTH_DICT[month] in ['September', 'April', 'June', 'November']:
        return 30
    elif MONTH_DICT[month] != 'February':
        return 31
    else:
        # It's February
        return 29 if is_leap_year() else 28


def progress_by_one_day(datedict):
    """
    Return a dict representing the next day.

    Input:
    <datedict>: {
        'day': <int> a number from 1-7
        'date': <int> a number from 1-31
        'month': <int> a number from 1-12
        'year': <int> any number
    }
    """
    day = datedict['day']
    date = datedict['date']
    month = datedict['month']
    year = datedict['year']

    new_datedict = {}

    new_datedict['day'] = day + 1 if day < 7 else 1

    num_days_in_month = get_num_days_in_month(month, year)

    if date == num_days_in_month:
        # Going from end of month to start of month
        new_datedict['date'] = 1
        if month == 12:
            # It's a new year! Going to January 1st
            new_datedict['month'] = 1
            new_datedict['year'] = year + 1
        else:
            # Same year, new month
            new_datedict['month'] = month + 1
            new_datedict['year'] = year

    else:
        # Staying in the same month
        new_datedict['date'] = date + 1
        new_datedict['month'] = month
        new_datedict['year'] = year

    return new_datedict


# Monday, January 1, 1900
current_date = {
    'day': DAY_DICT['Monday'],
    'date': 1,
    'month': 1,
    'year': 1900
}

# Progress to January 1, 1901 (to figure out the day of the week)
while (not (current_date['date'] == 1 and
            current_date['month'] == 1 and
            current_date['year'] == 1901)):
    current_date = progress_by_one_day(current_date)

sundays_on_first_day_of_month_count = 0

# End when we reach year 2001
while (current_date['year'] != 2001):
    if current_date['date'] == 1 and current_date['day'] == DAY_DICT['Sunday']:
        sundays_on_first_day_of_month_count += 1
    current_date = progress_by_one_day(current_date)

print(sundays_on_first_day_of_month_count)
