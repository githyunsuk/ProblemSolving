import sys
from itertools import combinations

N = int(input())
ingredient = [list(map(int, input().split())) for _ in range(N)]

comb = []
for i in range(1, N+1):
    comb.extend(combinations(ingredient, i))

minResult = sys.maxsize
for c in comb:
    sour = 1
    bitter = 0
    for i in c:
        sour *= i[0]
        bitter += i[1]
    tempResult = abs(sour - bitter)
    minResult = min(minResult, tempResult)
print(minResult)