#link: https://projecteuler.net/problem=34

# 145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.
#
# Find the sum of all numbers which are equal to the sum of the factorial of
# their digits.
#
# Note: as 1! = 1 and 2! = 2 are not sums they are not included.


import math

mapping = {}

for x in range(0,10):
    mapping[str(x)] = math.factorial(x)

print(mapping)

limit = 10000000
total = 0
for x in range(3, limit):
    if x == sum(map(lambda x: mapping[x], list(str(x)))):
        print(x)
        total += x
print(total)