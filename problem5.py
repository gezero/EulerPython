import primes

x=21

max_divisor=20

set =set()
for x in range(2,20):
	factors = primes.prime_factors(x)
	set.update(factors)
print(set)

multiplier = 1
for x in set:
	multiplier*=x
print(multiplier)

print(multiplier*3*2*2)