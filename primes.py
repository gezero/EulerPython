import math
__primes_sieve__ =[]
__max_sieve__=0
def primes_sieve(max):
	global __primes_sieve__
	global __max_sieve__
	if (max<__max_sieve__):
		return __primes_sieve__
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
	__primes_sieve__=primes
	__max_sieve__=max
	return primes
def prime_factors(number):
	if __max_sieve__ <= number:
		primes_sieve(number+1)
	if (number in __primes_sieve__):
		return [1,number]
	factors=[1]
	max_prime = math.floor(math.sqrt(number))+1
	for prime in __primes_sieve__:
		if prime>max_prime:
			return factors
		if number%prime ==0:
			factors.append(prime)
	return factors
def prime_factors_with_count(number):
	n =number
	if __max_sieve__ <= number:
		primes_sieve(number+1)
	factors={}
	for prime in __primes_sieve__:
		factors[prime]=0
		while number%prime ==0:
			number = number/prime
			factors[prime]+=1
		if number ==1:
			return factors
	raise ArithmeticError("We should not get here... The number {0} is not properly divisible...".format(n))


