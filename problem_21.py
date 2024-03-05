# amicable numbers https://projecteuler.net/problem=21

def get_divisors(n):
    divisors = []

    for i in range(1,int(n/2)+1):
        if n % i == 0:
            divisors.append(i)

    return divisors

def get_amicable(x):
    div = get_divisors(x)
    div_sum = sum(div)

    div_am = get_divisors(div_sum)
    div_am_sum = sum(div_am)

    if x == div_am_sum and x != div_sum:
        return True
    else:
        return False
    
amicable = []

for i in range(10000):
    if get_amicable(i):
        amicable.append(i)

print(sum(amicable))