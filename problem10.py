import primes

seed = primes.prime_seed(2000000)

sum =0
for x in seed:
	sum+=x

print(sum)