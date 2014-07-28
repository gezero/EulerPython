# link: https://projecteuler.net/problem=41
# We shall say that an n-digit number is pandigital if it makes use of all the
# digits 1 to n exactly once. For example, 2143 is a 4-digit pandigital and is
# also prime.

# What is the largest n-digit pandigital prime that exists?

import primes

template=['','1','12','123','1234','12345','123456','1234567']


def pandigital(n):
    x = ''.join(sorted(str(n)))
    return x == template[len(x)]

# sieve = primes.sieve(987654321)
sieve = primes.sieve(7654321) # rest is divisible by 3

for x in sieve:
    if pandigital(x):
        print(x)

