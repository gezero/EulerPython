# The following iterative sequence is defined for the set of positive integers:
#
# n → n/2 (n is even)
# n → 3n + 1 (n is odd)
#
# Using the rule above and starting with 13, we generate the following
# sequence:
#
# 13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
# It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.
#
# Which starting number, under one million, produces the longest chain?
#
# NOTE: Once the chain starts the terms are allowed to go above one million.

memory_limit = 99999999
memory = [0] * memory_limit
memory[1] = 1

def algorithm(n):
	if n >= memory_limit:
		return 1 + (algorithm(n // 2) if n % 2 == 0 else algorithm(n * 3 + 1))
	if memory[n] == 0:
		memory[n] = 1 + (algorithm(n // 2) if n % 2 == 0 else algorithm(n * 3 + 1))
	return memory[n]


print(algorithm(13))

current_max = 0
n=0
for x in range(1, 1000000):
	a = algorithm(x)
	if a > current_max:
		current_max = a
		n = x
print (current_max, n)
