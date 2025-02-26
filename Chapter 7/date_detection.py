﻿import re

def dateDetection(item):
    date = re.search(r'\d\d/\d\d/\d\d\d\d', item)
    return date

def dateChecker(item):
    day, month, year = item.split('/')
    if day == '00':
        return False
    elif month == '02':
        if int(day) > 28:
            return False
        else:
            return True
    elif month in ['04', '06', '09', '11']:
        if int(day) > 30:
            return False
        else:
            return True
    else:
        if int(day) > 31:
            return False
        else:
            return True

text = """Write a regular expression that can detect dates in the DD/MM/YYYY format.
Assume that the days range from 01 to 31, the months range from 01 to 12, and the years range from 1000 to 2999.
Note that if the day or month is a single digit, it’ll have a leading zero.
The regular expression doesn’t have to detect correct days for each month or for leap years; it will accept nonexistent dates like 31/02/2020 or 31/04/2021.
Then store these strings into variables named month, day, and year, and write additional code that can detect if it is a valid date.
April, June, September, and November have 30 days, February has 28 days, and the rest of the months have 31 days. February has 29 days in leap years.
Leap years are every year evenly divisible by 4, except for years evenly divisible by 100, unless the year is also evenly divisible by 400.
Note how this calculation makes it impossible to make a reasonably sized regular expression that can detect a valid date."""


print(dateChecker(dateDetection(text).group()))