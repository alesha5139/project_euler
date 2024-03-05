# non-abundant sums https://projecteuler.net/problem=23

def get_divisors(n):
    divisors = []

    for i in range(1,int(n/2)+1):
        if n % i == 0:
            divisors.append(i)

    return divisors

def get_abundant(n):
    divs = get_divisors(n)
    return sum(divs) > n

abs = []
for i in range(12,28124):
    if get_abundant(i):
        abs += [i]
print("GOT ABUNDANT") # track progress because I don't like just waiting

def can_be_written(n,abs):
    for x in abs:
        if x > n // 2:
            return False
        if n-x in abs:
            return True
    return False

t = 0

for i in range(28124):
    if i % 1000 == 0: # track progress because I don't like just waiting
        print(i)
    if not can_be_written(i,abs):
        t += i

print(t)