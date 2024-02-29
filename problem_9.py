# special pythagorean triplet https://projecteuler.net/problem=9

a = 1
b = 1

while True:
    while a < 1000:
        c = (a**2 + b**2)**0.5
        if a+b+c == 1000:
            print(a*b*c)
            exit()
        
        a += 1 
    a = 1 
    b += 1

    