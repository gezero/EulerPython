# link: https://projecteuler.net/problem=9

# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
#
# a^2 + b^2 = c^2
# For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.
#
# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.

maximum = 1000

for x in range(1, 334):
    for y in range(1, 501):
        numbers = sorted([x, y, maximum - x - y])
        if (numbers[0] * numbers[0] + numbers[1] * numbers[1]
                == numbers[2] * numbers[2]):
            print(numbers)
            print(numbers[0] * numbers[1] * numbers[2])
