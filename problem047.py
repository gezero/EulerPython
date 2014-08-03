#link: https://projecteuler.net/problem=47

# The first two consecutive numbers to have two distinct prime factors are:
#
# 14 = 2 × 7
# 15 = 3 × 5
#
# The first three consecutive numbers to have three distinct prime factors are:
#
# 644 = 2² × 7 × 23
# 645 = 3 × 5 × 43
# 646 = 2 × 17 × 19.
#
# Find the first four consecutive integers to have four distinct prime factors.
# What is the first of these numbers?


import primes
import sys

primes.sieve(140000)
target = 4

counter = 0
for x in range(2, 200000):
    # print(x, primes.factors(x))
    if (len(primes.factors(x)) >= target+1):
        counter += 1
    else:
        if (counter > 1):
            sys.stdout.write(str(counter))
            sys.stdout.flush()
        counter = 0
    if (counter == target):
        print('\n')
        print(x-target+1)
        break
