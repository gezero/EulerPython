# link: https://projecteuler.net/problem=37

# The number 3797 has an interesting property. Being prime itself, it is
# possible to continuously remove digits from left to right, and remain prime
# at each stage: 3797, 797, 97, and 7. Similarly we can work from right to left:
# 3797, 379, 37, and 3.
#
# Find the sum of the only eleven primes that are both truncatable from left to
# right and right to left.
#
# NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.

import primes

sieve = primes.sieve(1000000)
sieve_set = set(sieve)

def check(prime):
    if (prime < 10):
        return False
    p = str(prime)
    for x in range(len(p)):
        if not int(p[x:]) in sieve_set:
            return False
        if not int(p[:x+1]) in sieve_set:
            return False
    return True

total = 0
sum = 0
for prime in sieve:
    if check(prime):
        total += 1
        sum += prime
        print(prime)
    if total == 11:
        break
else:
    print("only " + str(total) + " primes found. Try to enlarge the sieve limit")
print(sum)