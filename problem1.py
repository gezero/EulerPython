# link: https://projecteuler.net/problem=1
#
# problem:
# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23. 
# Find the sum of all the multiples of 3 or 5 below 1000.

def count_multipliers_of_3_5(a,b):
	sum=0
	for x in range(a,b):
		if x%3==0 or x%5==0:
			sum+=x
			pass
	return sum

print(count_multipliers_of_3_5(1,10))
print(count_multipliers_of_3_5(1,1000))