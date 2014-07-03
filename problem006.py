#link: https://projecteuler.net/problem=6

#The sum of the squares of the first ten natural numbers is,

# 1^2 + 2^2 + ... + 10^2 = 385
# The square of the sum of the first ten natural numbers is,
#
# (1 + 2 + ... + 10)^2 = 552 = 3025
# Hence the difference between the sum of the squares of the first ten natural
# numbers and the square of the sum is 3025 − 385 = 2640.
#
# Find the difference between the sum of the squares of the first one hundred
# natural numbers and the square of the sum.

total = 0
squareSum = 0
for x in range(1, 101):
    total += x
    squareSum += x * x
print(total * total)
print(squareSum)
print(total * total - squareSum)
