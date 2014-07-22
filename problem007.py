#link: https://projecteuler.net/problem=7

# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see
# that the 6th prime is 13.

# What is the 10 001st prime number?

import primes

sieve = primes.sieve(1000000)

print(len(sieve))

print(sieve[0])
print(sieve[5])
print(sieve[10000])
