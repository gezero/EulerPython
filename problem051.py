# link: https://projecteuler.net/problem=51

# By replacing the 1st digit of the 2-digit number *3, it turns out that six of
# the nine possible values: 13, 23, 43, 53, 73, and 83, are all prime.
#
# By replacing the 3rd and 4th digits of 56**3 with the same digit, this 5-digit
# number is the first example having seven primes among the ten generated
# numbers, yielding the family: 56003, 56113, 56333, 56443, 56663, 56773, and
# 56993. Consequently 56003, being the first member of this family, is the
# smallest prime with this property.
#
# Find the smallest prime which, by replacing part of the number (not
# necessarily adjacent digits) with the same digit, is part of an eight prime
# value family.

import primes
import itertools

sieve = primes.sieve(1000000)



pset = set(sieve)


limit = 2
max_counter = 0
def check_string(string,p=False):
    global max_counter
    global limit
    counter = 0
    for i in range(10):
        x = int(string.replace('*',str(i)))
        if (x in pset):
            if (p):
                print(x)
                p = False
            if i-counter+1 > max_counter:
                max_counter = i-counter+1
                print(max_counter,string)
            else:
                pass
        else:
            counter += 1
        if counter > limit:
            return False
    return True


# print(check_string("56**3"))
# print(check_string("*2*3*3",True))

source = ['*','*','*']
endings = ['1','3','7','9']
for i in range(1,1000):
# for i in range(56,57):
    s = str(i)
    ss = ''.join(sorted(s))
    if s == ss:
        perm_source = source + list(str(i))
        for perm in itertools.permutations(perm_source):
            for ending in endings:
                string = ''.join(perm) +ending
                if check_string(string):
                    # print(perm, ending, string)
                    check_string(string,True)
                    exit()