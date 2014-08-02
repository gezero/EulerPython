# link: https://projecteuler.net/problem=46
# It was proposed by Christian Goldbach that every odd composite number can be
# written as the sum of a prime and twice a square.
#
# 9 = 7 + 2×12
# 15 = 7 + 2×22
# 21 = 3 + 2×32
# 25 = 7 + 2×32
# 27 = 19 + 2×22
# 33 = 31 + 2×12
#
# It turns out that the conjecture was false.
#
# What is the smallest odd composite that cannot be written as the sum of a
# prime and twice a square?

import primes

sieve = primes.sieve(10000)

sums = set()

for i in range(200):
    square = 2*i*i
    for prime in sieve:
        sums.add(prime + square)


for i in range(3, 10000, 2):
    if not i in sums:
        print(i)
