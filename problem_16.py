# power digit sums https://projecteuler.net/problem=16

x = 2**1000
s = str(x)

total = 0
for i in s:
    total += int(i)

print(total)