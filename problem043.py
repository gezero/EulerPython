#link: https://projecteuler.net/problem=43

# The number, 1406357289, is a 0 to 9 pandigital number because it is made up of
# each of the digits 0 to 9 in some order, but it also has a rather interesting
# sub-string divisibility property.
#
# Let d1 be the 1st digit, d2 be the 2nd digit, and so on. In this way, we note
# the following:
#
# d2d3d4=406 is divisible by 2
# d3d4d5=063 is divisible by 3
# d4d5d6=635 is divisible by 5
# d5d6d7=357 is divisible by 7
# d6d7d8=572 is divisible by 11
# d7d8d9=728 is divisible by 13
# d8d9d10=289 is divisible by 17
#
# Find the sum of all 0 to 9 pandigital numbers with this property.

numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
primes = [2, 3, 5, 7, 11, 13, 17]

def check_digits(i, digits):
    for k in range(i,7):
        prime = primes[k]
        x = digits[k+1]*100 + digits[k+2] *10 + digits[k+3]
        if (not x % prime == 0):
            return False
    return True

def choose_digit(i, digits, rest):
    total = 0
    if (len(rest) == 1):
        for x in rest:
            digits[0] = x
            num = ''.join(map(lambda x: str(x),digits))
            digits[0] = None
            print(num)
            return int(num)
    for x in rest:
        digits[i] = x
        new_rest = rest - set([x])
        if (check_digits(i-1, digits)):
            total += choose_digit(i-1, digits, new_rest)
        else:
            digits[i] = None
    else:
        digits[i] = None
    return total

print(choose_digit(9, [None]*10, set(numbers)))
