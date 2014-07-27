# link: https://projecteuler.net/problem=40

# An irrational decimal fraction is created by concatenating the positive
# integers:
#
# 0.123456789101112131415161718192021...
#
# It can be seen that the 12th digit of the fractional part is 1.
#
# If dn represents the nth digit of the fractional part, find the value of the
# following expression.
#
# d1 × d10 × d100 × d1000 × d10000 × d100000 × d1000000

import operator
from functools import reduce


def n_th_digit(n):
    lenght = 1
    while True:
        number_count = 10**(lenght-1) * 9
        total_digits = number_count * lenght
        if n <= total_digits:
            d = (n-1) // lenght
            pos = (n-1) % lenght
            return int(str(10**(lenght-1) + d)[pos])
        n -= total_digits
        lenght += 1

digits = [1, 10, 100, 1000, 10000, 100000, 1000000]

print(reduce(operator.mul,(map(lambda x: n_th_digit(x),digits))))

