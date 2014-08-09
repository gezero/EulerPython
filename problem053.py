# link: https://projecteuler.net/problem=53


# There are exactly ten w# ays of selecting three from five, 12345:
#
# 123, 124, 125, 134, 135# , 145, 234, 235, 245, and 345
#
# In combinatorics, we us# e the notation, 5C3 = 10.
#
# In general,#
#
# nCr =  n! /(r!(n−r)!), # where r ≤ n, n! = n×(n−1)×...×3×2×1, and 0! = 1.
# It is not until n = 23,#  that a value exceeds one-million: 23C10 = 1144066.
#
# How many, not necessari# ly distinct, values of  nCr, for 1 ≤ n ≤ 100, are
# greater than one-million?


def comb(n, k):
    if 0 <= k <= n:
        ntok = 1
        ktok = 1
        for t in range(1, min(k, n - k) + 1):
            ntok *= n
            ktok *= t
            n -= 1
        return ntok // ktok
    else:
        return 0

count = 0
for x in range(1, 101):
    for y in range(x, 101):
        if comb(y,x) > 1000000:
            count += 1
print(count)
