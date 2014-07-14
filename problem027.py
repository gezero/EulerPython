# link: https://projecteuler.net/problem=27

# Euler discovered the remarkable quadratic formula:
#
# n² + n + 41
#
# It turns out that the formula will produce 40 primes for the consecutive
# values n = 0 to 39. However, when n = 40, 402 + 40 + 41 = 40(40 + 1) + 41 is
# divisible by 41, and certainly when n = 41, 41² + 41 + 41 is clearly divisible
# by 41.
#
# The incredible formula  n² − 79n + 1601 was discovered, which produces 80
# primes for the consecutive values n = 0 to 79. The product of the
# coefficients, −79 and 1601, is −126479.
#
# Considering quadratics of the form:
#
# n² + an + b, where |a| < 1000 and |b| < 1000
#
# where |n| is the modulus/absolute value of n
# e.g. |11| = 11 and |−4| = 4
# Find the product of the coefficients, a and b, for the quadratic expression
# that produces the maximum number of primes for consecutive values of n,
# starting with n = 0.

import primes


def count(n, a, b):
    return n*n + n*a + b


def count_length(a,b):
        n = 0
        while primes.is_prime(count(n, a, b)):
            n += 1
        return n


print(count_length(1, 41))
print(count_length(-79, 1601))

besta =- 1000
bestb =- 1000
amount = 0
for a in range(-999, 1000):
    if a % 100 == 0:
        print(a)
    for b in range(-999, 1000):
        n = count_length(a, b)
        if (n > amount):
            print(a,b,n,a*b)
            amount =n
