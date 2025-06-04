from itertools import combinations

import sys

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
points = [(i, j) for i in range(1, N-1) for j in range(1, N-1)]


minCost = sys.maxsize
for comb in combinations(points, 3):
    lst = []
    for c in comb:
        i, j = c
        lst.append((i,j))
        lst.append((i+1,j))
        lst.append((i,j+1))
        lst.append((i-1,j))
        lst.append((i,j-1))
    if len(set(lst)) != 15:
        continue
    cost = 0
    for l in lst:
        a, b = l
        cost += arr[a][b]
    minCost = min(minCost, cost)

print(minCost)
