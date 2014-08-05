#link: https://projecteuler.net/problem=48

# The series, 1^1 + 2^2 + 3^3 + ... + 10^10 = 10405071317.

# Find the last ten digits of the series, 1^1 + 2^2 + 3^3 + ... + 1000^1000.


mod = 10**10
def last10DigitsNtoN(n):
    total = 1
    for i in range(n):
        total = (total *n) % mod
    return total


total = 0
for i in range(1,1001):
    total += last10DigitsNtoN(i)
print(total % mod)