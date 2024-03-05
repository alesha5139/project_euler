# factorial digit sum https://projecteuler.net/problem=20

import math

s = str(math.factorial(100))

total = 0 

for x in s:
    total += int(x)

print(total)