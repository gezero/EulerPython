import math
def prime_seed(max):
	numbers=[0]*max
	primes=[]
	sqrt = round(math.sqrt(max))+1;
	for x in range(2,sqrt):
		if numbers[x]==1:
			continue
		primes.append(x)
		for y in range(x+x,max,x):
			numbers[y]=1
	for x in range(sqrt,max):
		if numbers[x] == 0:
			primes.append(x)
		pass
	return primes	
def prime_factors(primes,number):
	factors=[1]
	for prime in primes:
		if number%prime ==0:
			factors.append(prime)
	return factors
def prime_factors_with_count(primes,number):
	factors=[1]
