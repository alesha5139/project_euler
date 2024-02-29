# sum square difference https://projecteuler.net/problem=6

squares = []
for i in range(1,101):
    squares += [i**2]
sum_square = sum(squares)

square_sum = sum(range(1,101))**2

print(square_sum-sum_square)