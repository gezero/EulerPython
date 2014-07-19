# link: https://projecteuler.net/problem=24

# A permutation is an ordered arrangement of objects. For example, 3124 is one
# possible permutation of the digits 1, 2, 3 and 4. If all of the permutations
# are listed numerically or alphabetically, we call it lexicographic order. The
# lexicographic permutations of 0, 1 and 2 are:
# 012   021   102   120   201   210
# What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4,
# 5, 6, 7, 8 and 9?

import math

factorials = list(math.factorial(x) for x in range(0, 10))[::-1]


def write_ordering(ordering):
    result = []
    ordering -= 1
    numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    numbers_index = 0
    factorials_index = 0
    while ordering > 0:
        if (ordering >= factorials[factorials_index]):
            ordering -= factorials[factorials_index]
            numbers_index += 1
        if (ordering < factorials[factorials_index]):
            result.append(numbers[numbers_index])
            numbers.remove(numbers[numbers_index])
            factorials_index += 1
            numbers_index = 0
    for x in numbers:
        result.append(x)
    return result

print(write_ordering(2))
print(write_ordering(1))
print(write_ordering(1000000))
print(write_ordering(math.factorial(10)))
