# link: https://projecteuler.net/problem=22

# Using names.txt (right click and 'Save Link/Target As...'), a 46K text file
# containing over five-thousand first names, begin by sorting it into
# alphabetical order. Then working out the alphabetical value for each name,
# multiply this value by its alphabetical position in the list to obtain a name
# score.
# For example, when the list is sorted into alphabetical order, COLIN, which is
# worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So, COLIN
# would obtain a score of 938 × 53 = 49714.

# What is the total of all the name scores in the file?

import re

content = []
with open('problem022names.txt', 'r') as f:
    # the following command is splitting the input file into the content list.
    # The lambda function is responsible for splitting one line into list of
    # numbers.
    content = sorted(re.sub('"', '', f.readline()).split(","))

print(content[937])


def name_value(name):
    total = 0
    for c in list(name):
        total += ord(c) - ord('A') + 1
    return total

print(name_value(content[937]))


total = 0
for i, name in enumerate(content):
    total += (i+1) * name_value(name)
print(total)
