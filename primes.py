import math
__primes_sieve__ = []
__set_primes_sieve__ = {}
__max_sieve__ = 0


def primes_sieve(limit):
    global __primes_sieve__
    global __max_sieve__
    global __set_primes_sieve__
    if (limit < __max_sieve__):
        return __primes_sieve__
    numbers = [0] * limit
    primes = []
    sqrt = round(math.sqrt(limit)) + 1
    for x in range(2, sqrt):
        if numbers[x] == 1:
            continue
        primes.append(x)
        for y in range(x + x, limit, x):
            numbers[y] = 1
    for x in range(sqrt, limit):
        if numbers[x] == 0:
            primes.append(x)
        pass
    __primes_sieve__ = primes
    __set_primes_sieve__ = set(__primes_sieve__)
    __max_sieve__ = limit
    return primes


def prime_factors(number):
    if __max_sieve__ <= number:
        primes_sieve(number + 1)
    if (number in __primes_sieve__):
        return [1, number]
    factors = [1]
    max_prime = math.floor(math.sqrt(number)) + 1
    for prime in __primes_sieve__:
        if prime > max_prime:
            return factors
        if number % prime == 0:
            factors.append(prime)
    return factors


def prime_factors_with_count(number):
    n = number
    if n == 1:
        return {}
    if __max_sieve__ <= number:
        primes_sieve(2*number + 1)
    factors = {}
    for prime in __primes_sieve__:
        factors[prime] = 0
        while number % prime == 0:
            number = number // prime
            factors[prime] += 1
        if number == 1:
            return factors
        if prime * prime > number:
            factors[number] = 1
            return factors
    raise ArithmeticError("We should not get here... The number {0} is not properly divisible...".format(n))


def all_divisors(n):
    divisors = {1}
    factors = prime_factors_with_count(n)
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


def is_abundant(number):
    return number < sum(proper_divisors(number))


def is_prime(number):
    if __max_sieve__ <= number:
        primes_sieve(2*number + 1)
    return number in __set_primes_sieve__
