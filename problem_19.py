# counting sundays https://projecteuler.net/problem=19

sundays = 0

# 1 is Sunday, 2 is Monday, 3 is Tuesday, etc. and 1901.01.01 was a tuesday
day = 3
date = 1
month = 1
year = 1901

while year != 2001:
    if day == 1 and date == 1:
        sundays += 1

    # move the day forwards
    day += 1
    if day == 1:
        sundays += 1
    if day == 8:
        day = 1

    # move the date forwards
    date += 1
    if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
        if date == 32:
            date = 1
            month += 1
    elif month == 4 or month == 6 or month == 9 or month == 11:
        if date == 31:
            date = 1
            month += 1
    elif month == 2 and year % 4 == 0:
        if date == 30:
            date = 1
            month += 1
    else:
        if date == 29:
            date = 1
            month += 1
    if month == 13:
        month = 1
        year += 1

print(sundays)