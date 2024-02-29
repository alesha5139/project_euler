# smallest multiple https://projecteuler.net/problem=5

import math

def lcm(n,m):
    return (n*m)//math.gcd(n,m)

sml_mult = 1

for i in range(1,21):
    sml_mult = lcm(sml_mult,i)

print(sml_mult)
