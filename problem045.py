#link: https://projecteuler.net/problem=45
# Triangle, pentagonal, and hexagonal numbers are generated by the following
# formulae:
#
# Triangle        Tn=n(n+1)/2     1, 3, 6, 10, 15, ...
# Pentagonal      Pn=n(3n−1)/2        1, 5, 12, 22, 35, ...
# Hexagonal       Hn=n(2n−1)      1, 6, 15, 28, 45, ...
# It can be verified that T285 = P165 = H143 = 40755.
#
# Find the next triangle number that is also pentagonal and hexagonal.


pentagonal = set()
hexagonal = set()

count = 0
for n in range(1, 100000):
    triangle = n*(n+1) // 2
    pentagonal.add(n*(3*n - 1) // 2)
    hexagonal.add(n*(2*n - 1))
    if triangle in pentagonal and triangle in hexagonal:
        print(n, triangle)
        count += 1
        if (count == 3):
            print(count)
            exit()
