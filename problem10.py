import primes

sieve = primes.primes_sieve(2000000)

sum =0
for x in sieve:
	sum+=x

print(sum)