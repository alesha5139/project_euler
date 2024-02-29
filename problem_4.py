# Largest Palindrome Product https://projecteuler.net/problem=4

x1 = 999
x2 = 999
m_prod = 0

def palindrome(p):
    s = str(p)
    pal = True
    for i in range(len(s)):
        if s[i] != s[len(s)-i-1]:
            pal = False
    return pal

while x1 > 99:
    while x2 > 99:
        prod = x1*x2
        if palindrome(prod) and prod > m_prod:
            m_prod = prod
        x2 -= 1
    x2 = 999
    x1 -= 1

print(m_prod)