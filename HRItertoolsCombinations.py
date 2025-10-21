from itertools import combinations

s, k = input().split()
k = int(k)

s_sorted = sorted(s)

for i in range(1, k+1):  
    for p in combinations(s_sorted, i):
        print(''.join(p))
