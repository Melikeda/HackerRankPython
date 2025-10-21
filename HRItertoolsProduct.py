from itertools import product

A = list(map(int, input().split()))
B = list(map(int, input().split()))

for cartesian in product(A, B):
    print(cartesian, end=' ')
