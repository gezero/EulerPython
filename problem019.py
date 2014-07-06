# link: https://projecteuler.net/problem=19

# You are given the following information, but you may prefer to do some
# research for yourself.
#
# * 1 Jan 1900 was a Monday.
# * Thirty days has September,
#   April, June and November.
#   All the rest have thirty-one,
#   Saving February alone,
#   Which has twenty-eight, rain or shine.
#   And on leap years, twenty-nine.
# * A leap year occurs on any year evenly divisible by 4, but not on a century
#   unless it is divisible by 400.
#
# How many Sundays fell on the first of the month during the twentieth century
# (1 Jan 1901 to 31 Dec 2000)?

import datetime

tho = datetime.timedelta(days=31)
th = datetime.timedelta(days=30)
twe = datetime.timedelta(days=28)
twn = datetime.timedelta(days=29)

months = [tho, twe, tho, th, tho, th, tho, tho, th, tho, th, tho]

date = datetime.datetime(1900, 1, 1)
startDate = datetime.datetime(1901, 1, 1)
endDate = datetime.datetime(2000, 12, 31)

count = 0
while date < endDate:
    for m in months:
        if m == twe:
            if date.year % 4 == 0 and date.year % 100 != 0:
                m = twn
            if date.year % 400 == 0:
                m = twn
        date += m
        if startDate < date:
            if date.weekday() == 6:
                print(date)
                count += 1
print(count)
