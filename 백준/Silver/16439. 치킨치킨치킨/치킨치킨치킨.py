from itertools import combinations

N, M = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(N)]

maxSum = 0
for a, b, c in combinations(range(M), 3):
    tempSum = 0
    for i in range(N):
        tempSum += max(lst[i][a], lst[i][b], lst[i][c])
    maxSum = max(maxSum, tempSum)
print(maxSum)
