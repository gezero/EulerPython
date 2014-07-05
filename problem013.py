#link: https://projecteuler.net/problem=13

# Work out the first ten digits of the sum of the following one-hundred 50-digit
# numbers.

numbers = []

with open('problem013.data', 'r') as f:
    numbers = list(map(int, f.readlines()))

print(sum(numbers))
print(str(sum(numbers))[0:10])
