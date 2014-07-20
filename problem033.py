# link: https://projecteuler.net/problem=33

# The fraction 49/98 is a curious fraction, as an inexperienced mathematician in
# attempting to simplify it may incorrectly believe that 49/98 = 4/8, which is
# correct, is obtained by cancelling the 9s.
#
# We shall consider fractions like, 30/50 = 3/5, to be trivial examples.
#
# There are exactly four non-trivial examples of this type of fraction, less
# than one in value, and containing two digits in the numerator and
# denominator.
#
# If the product of these four fractions is given in its lowest common terms,
# find the value of the denominator.

import primes


def simplify(n, d):
    gcd = primes.gcd(n, d)
    return (n // gcd, d // gcd)

def wronglySimplify(n, d):
    digits_n = list(str(n))
    digits_d = list(str(d))
    intersection = list(set(digits_n).intersection(digits_d))
    if len(intersection) == 1:
        digits_n.remove(intersection[0])
        digits_d.remove(intersection[0])
    return (int(''.join(digits_n)), int(''.join(digits_d)))

tn = 1
td = 1
for n in range(10, 99):
    for d in range(n+1, 100):
        if d % 10 > 0 and n % 10 > 0:
            n1 = wronglySimplify(n, d)
            if (n1[0] < n):
                n2 = simplify(n, d)
                n3 = simplify(n1[0],n1[1])
                if n2[0] == n3[0] and n2[1] == n3[1]:
                    print(n,d, n1)
                    tn *= n1[0]
                    td *= n1[1]



print (simplify(tn,td))

