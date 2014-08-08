# link: https://projecteuler.net/problem=52

# It can be seen that the number, 125874, and its double, 251748, contain
# exactly the same digits, but in a different order.

# Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x,
# contain the same digits.


for i in range(1, 1000000):
    si = sorted(str(i))
    for j in range(2, 7):
        if si != sorted(str(j*i)):
            break
    else:
        print(i)
        exit()
