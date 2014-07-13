# link: https://projecteuler.net/problem=26

# A unit fraction contains 1 in the numerator. The decimal representation of the
# unit fractions with denominators 2 to 10 are given:
#
# 1/2 =   0.5
# 1/3 =   0.(3)
# 1/4 =   0.25
# 1/5 =   0.2
# 1/6 =   0.1(6)
# 1/7 =   0.(142857)
# 1/8 =   0.125
# 1/9 =   0.(1)
# 1/10    =   0.1
# Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It can be
# seen that 1/7 has a 6-digit recurring cycle.
#
# Find the value of d < 1000 for which 1/d contains the longest recurring cycle
# in its decimal fraction part.


import sys


def find_recuring_cycle(number):
    remainders = [1]
    # sys.stdout.write('0.')
    numerator = 10
    for x in range(0, number):
        remainder = numerator % number
        # sys.stdout.write(str(numerator // number))
        if remainder in remainders:
            position = [i for i, x in enumerate(remainders) if x == remainder][0]
            # sys.stdout.write('\n')
            return len(remainders) - position
        remainders.append(remainder)
        numerator = remainder*10

maximum = 0
when = 0
for x in range(2,1000):
    cycle = find_recuring_cycle(x)
    if (cycle>maximum):
        maximum = cycle 
        when =x
        print(when,cycle)

