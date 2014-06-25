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
# number = 13195
number = 600851475143 

max_prime = round(math.sqrt(number))
primes = prime_seed(max_prime)

def prime_factors(primes,number):
	factors=[]
	for prime in primes:
		if number%prime ==0:
			factors.append(prime)
	return factors
	
factors = prime_factors(primes, number)
print(factors)
print(factors[-1])