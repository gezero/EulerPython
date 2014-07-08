# link: https://projecteuler.net/problem=21

# Let d(n) be defined as the sum of proper divisors of n (numbers less than n
# which divide evenly into n). If d(a) = b and d(b) = a, where a ≠ b, then a
# and b are an amicable pair and each of a and b are called amicable numbers.
#
# For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55
# and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71
# and 142; so d(284) = 220.
#
# Evaluate the sum of all the amicable numbers under 10000.


import primes


def all_divisors(n):
    divisors = {1}
    factors = primes.prime_factors_with_count(n)
    for (k, v) in factors.items():
        for x in range(0, v):
            new_divisors = set(y*k for y in divisors)
            new_divisors.update(divisors)
            divisors = new_divisors
    return divisors


def proper_divisors(n):
    divisors = all_divisors(n)
    divisors.remove(n)
    return divisors


total = 0
sums = [0]
for x in range(1, 10001):
    sums.append(sum(proper_divisors(x)))
    if sums[x] < x:
        if sums[sums[x]] == x :
            print(x, sums[x])
            total += x + sums[x]
print(total)
