#link: https://projecteuler.net/problem=50

# The prime 41, can be written as the sum of six consecutive primes:
#
# 41 = 2 + 3 + 5 + 7 + 11 + 13
# This is the longest sum of consecutive primes that adds to a prime below
# one-hundred.
#
# The longest sum of consecutive primes below one-thousand that adds to a prime,
# contains 21 terms, and is equal to 953.
#
# Which prime, below one-million, can be written as the sum of the most
# consecutive primes?


import primes

stop = 1000000

sieve = primes.sieve(stop)

pset = set(sieve)

max = 0
sums = [0]*len(sieve)
for counter in range(0, stop):
    for i, prime in enumerate(sieve[counter:]):
        sums[i] += prime
        if sums[i] >= stop:
            break
        if counter > max and sums[i] in pset:
            print(counter + 1, sums[i])
            counter = max
