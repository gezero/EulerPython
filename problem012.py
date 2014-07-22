#link: https://projecteuler.net/problem=12

# The sequence of triangle numbers is generated by adding the natural numbers.
# So the 7th triangle number would be 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28. The first
# ten terms would be:
#
# 1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...
#
# Let us list the factors of the first seven triangle numbers:
#
#  1: 1
#  3: 1,3
#  6: 1,2,3,6
# 10: 1,2,5,10
# 15: 1,3,5,15
# 21: 1,3,7,21
# 28: 1,2,4,7,14,28
# We can see that 28 is the first triangle number to have over five divisors.
#
# What is the value of the first triangle number to have over five hundred
# divisors?

import primes

def count_divisors(n):
    prime_factors = primes.factors_with_count(n)
    factors = 1
    for x in prime_factors.keys():
        factors *= prime_factors[x]+1
    return factors

n = 0
total = 0
divisors = 0

current_max = 0

while divisors < 500:
    n += 1
    total += n
    divisors = count_divisors(total)
    if divisors > current_max:
        current_max = divisors
        print(divisors,total)
