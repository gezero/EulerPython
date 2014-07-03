#link: https://projecteuler.net/problem=10

# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
# Find the sum of all the primes below two million.

import primes

sieve = primes.primes_sieve(2000000)

total = 0
for x in sieve:
    total += x

print(total)
