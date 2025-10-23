n = int(input())
M = set(map(int, input().split()))

m = int(input())
N = set(map(int, input().split()))

set3 = M ^ N

for value in sorted(set3):
    print(value)
