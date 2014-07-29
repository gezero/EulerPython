#link: https://projecteuler.net/problem=42

# The nth term of the sequence of triangle numbers is given by, tn = ½n(n+1); so
# the first ten triangle numbers are:
#
# 1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...
#
# By converting each letter in a word to a number corresponding to its
# alphabetical position and adding these values we form a word value. For
# example, the word value for SKY is 19 + 11 + 25 = 55 = t10. If the word value
# is a triangle number then we shall call the word a triangle word.
#
# Using words.txt (right click and 'Save Link/Target As...'), a 16K text file
# containing nearly two-thousand common English words, how many are triangle
# words?

import re

triangle_numbers = set()

for i in range(1, 1000):
    triangle_numbers.add(i*(i+1)//2)


def isTriangleWord(w):
    total = sum(map(lambda x: ord(x)-ord('A')+1, list(w)))
    return total in triangle_numbers

content = []
with open('problem042words.txt', 'r') as f:
    # the following command is splitting the input file into the content list.
    # The lambda function is responsible for splitting one line into list of
    # numbers.
    content = sorted(re.sub('"', '', f.readline()).split(","))

count = 0
for word in content:
    if  isTriangleWord(word):
        count+=1
print(count)
