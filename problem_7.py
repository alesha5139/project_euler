# probem 7 https://projecteuler.net/problem=7
# HAD TO LOOK THIS ONE UP

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def prime_generator():
    num = 2
    count = 0
    while True:
        if is_prime(num):
            count += 1
            yield num
        num += 1

def nth_prime(n):
    prime_gen = prime_generator()
    for _ in range(n):
        prime = next(prime_gen)
    return prime

# Finding the 10001st prime
n = 10001
print(nth_prime(n))
