import primes

sieve = primes.primes_sieve(100000)

n=0
sum=0
factors =0

while factors<500:
	n+=1
	sum+=n
	prime_factors=primes.prime_factors_with_count(sum)
	factors =1
	for x in prime_factors.keys():
		factors*=prime_factors[x]+1

print(prime_factors)
print(factors)
print(n)
print(sum)