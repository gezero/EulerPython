# link: https://projecteuler.net/problem=32

# We shall say that an n-digit number is pandigital if it makes use of all the
# digits 1 to n exactly once; for example, the 5-digit number, 15234, is 1
# through 5 pandigital.
#
# The product 7254 is unusual, as the identity, 39 × 186 = 7254, containing
# multiplicand, multiplier, and product is 1 through 9 pandigital.
#
# Find the sum of all products whose multiplicand/multiplier/product identity
# can be written as a 1 through 9 pandigital.
#
# HINT: Some products can be obtained in more than one way so be sure to only
# include it once in your sum.

import functools
import itertools

products = set()


def number(a):
    if (len(a) == 1):
        return a[0]
    return functools.reduce(lambda x, y: 10*x+y, a)

def check_ordering(perm):
    for p in range(4, len(perm)-4):  #the magical 4, -4 and -2 are just small optimizations for this particular case
        product = number(perm[0:p])
        for l in range(p+1, len(perm)-2):
            left = number(perm[p:l])
            right = number(perm[l:])
            if (left * right == product):
                products.add(product)
                print(product, '=', left, "*",right)

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for perm in itertools.permutations(numbers):
    check_ordering(perm)
print(products)
print(sum(products))
