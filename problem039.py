# link: https://projecteuler.net/problem=39

# If p is the perimeter of a right angle triangle with integral length sides,
# {a,b,c}, there are exactly three solutions for p = 120.
#
# {20,48,52}, {24,45,51}, {30,40,50}
#
# For which value of p ≤ 1000, is the number of solutions maximised?

import primes

def triplet(m, n, k = 1):
    return (k*(m*m-n*n), k*2*m*n, k*(m*m+n*n))

counts = [0] * 1001

for n in range(1,40):
    for m in range(n,40):
        if primes.coprime(m,n) and (m - n) % 2 ==1:
            k=1
            t = triplet(m, n, k)
            while sum(t) <= 1000:
                counts[sum(t)] += 1
                k += 1
                t = triplet(m,n,k)
            if k == 1:
                break

print(counts.index(max(counts)))
