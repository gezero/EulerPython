#link: https://projecteuler.net/problem=49

# The arithmetic sequence, 1487, 4817, 8147, in which each of the terms
# increases by 3330, is unusual in two ways: (i) each of the three terms are
#prime, and, (ii) each of the 4-digit numbers are permutations of one another.
#
# There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes,
# exhibiting this property, but there is one other 4-digit increasing sequence.
#
# What 12-digit number do you form by concatenating the three terms in this
# sequence?


import primes
import itertools

sieve = primes.sieve(10000)



def check_group(group):
    for combination in itertools.combinations(group, 3):
        if (combination[0] +combination[2] == 2*combination[1]):
            print(''.join(map(lambda x: str(x),combination)))

groups = {}
for prime in sieve:
    if prime > 1000:
        group = ''.join(sorted(str(prime)))
        if not group in groups:
            groups[group] = []
        groups[group].append(prime)

for key, group in groups.items():
    if len(group) >= 3:
        check_group(group)
