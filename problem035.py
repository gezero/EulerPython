#link: https://projecteuler.net/problem=35


# The number, 197, is called a circular prime because all rotations of the
# digits: 197, 971, and 719, are themselves prime.
#
# There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71,
# 73, 79, and 97.
#
# How many circular primes are there below one million?

import primes
import copy

sieve = set(primes.sieve(1000000))

def circular(p):
    s = str(p)
    for n in range(0, len(s)):
        p1 = int(s[n:] + s[:n])
        if not p1 in sieve:
            return False
    return True

total = 0
for prime in sieve:
    if circular(prime):
        total += 1
print(total)
