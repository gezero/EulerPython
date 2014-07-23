# link https://projecteuler.net/problem=36

# The decimal number, 585 = 1001001001 (binary), is palindromic in both bases.
#
# Find the sum of all numbers, less than one million, which are palindromic in
# base 10 and base 2.
#
# (Please note that the palindromic number, in either base, may not include
# leading zeros.)


def check_binary(i):
    b = bin(i)[2:]
    return b == b[::-1]

total = 0
for i in range(1000):
    if i % 10 == 0:
        continue
    i_s = str(i)
    n = int(i_s[::-1]+i_s[1:])
    if check_binary(n):
        total += n
    for x in range(0, 6-2*len(i_s)+1):
        nulls = "0" * x
        n = int(i_s[::-1] + nulls + i_s)
        if check_binary(n):
            total += n
else:
    print(total)

