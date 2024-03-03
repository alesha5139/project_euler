# lattice paths https://projecteuler.net/problem=15

import math

def lattice_paths(n):
    return math.factorial(2*n)/(math.factorial(n)**2)

print(lattice_paths(20))