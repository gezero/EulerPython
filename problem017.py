#link: https://projecteuler.net/problem=17

# If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.
# If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?
# NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage.

import re


ones = [None, "one", "two", "three", "four", "five", "six", "seven", "eight",
        "nine"]
teens = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen",
         "sixteen", "seventeen", "eighteen", "nineteen"]
tens = [None, "ten", "twenty", "thirty", "forty", "fifty", "sixty", "seventy",
        "eighty", "ninety"]


def get_number(n):
    if n < 10:
        return ones[n]
    if n < 20:
        return teens[n-10]
    if n < 100:
        if n % 10 == 0:
            return tens[n // 10]
        return tens[n // 10] + " " + ones[n % 10]
    if n < 1000:
        if n % 100 == 0:
            return ones[n // 100] + " hundred"
        return ones[n // 100] + " hundred and " + get_number(n % 100)
    return "one thousand"

print(get_number(7))
print(get_number(17))
print(get_number(70))
print(get_number(77))
print(get_number(700))
print(get_number(707))
print(get_number(717))
print(get_number(770))
print(get_number(777))

print(get_number(342))
print(len(get_number(342)))

print(get_number(115))
print(len(get_number(115)))

total = 0
for x in range(1, 1001):
    total += len(re.sub(" ", "", get_number(x)))

print(total)
