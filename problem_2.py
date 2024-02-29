# even fibonacci https://www.youtube.com/watch?v=2_sjQ-k1db8

t = 0
prev=0
current = 1
fib = 1

while fib < 4000000:
    if fib % 2 == 0:
        t += current
    fib = current + prev
    prev = current
    current = fib

print(t)