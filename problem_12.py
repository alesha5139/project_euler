# highly divisible triangular number https://projecteuler.net/problem=12

def get_triangle(n):
    return n * (n + 1) / 2

found = False

n = 1
while not found:
    triangle_number = int(get_triangle(n))
    divisors = 0

    for i in range(1, int(triangle_number**0.5)+1):
        if triangle_number % i == 0:
            if i == triangle_number**0.5:
                divisors += 1
            else:
                divisors += 2
    
    if divisors > 500:
        found = True
        print(f'FOUND TRIANGLE NUMBER: {triangle_number}')

    print(triangle_number)
    n += 1

# 76576500