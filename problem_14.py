# collatz https://projecteuler.net/problem=14

def collatz(n):
    if n % 2 == 0:
        return n/2
    else:
        return 3*n + 1


max = 0
max_n = 0
seen = {}

for i in range(1,1000000):
    count = 1
    n = i

    while n != 1:
        if n not in seen:
            n = collatz(n)
            count += 1
        else:
            count += seen[n]
            n = 1
            if max < count:
                max = count
                max_n = i
    
    seen[i] = count


print(max_n, max)