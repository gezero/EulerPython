#link: https://projecteuler.net/problem=4

# A palindromic number reads the same both ways. The largest palindrome made
# from the product of two 2-digit numbers is 9009 = 91 × 99.
# Find the largest palindrome made from the product of two 3-digit numbers.

start = 100
end = 1000

max = 0
for x in range(start, end):
    for y in range(start, end):
        val = x*y
        if str(val) == str(val)[::-1]:
            if val > max:
                max = val

print(max)
