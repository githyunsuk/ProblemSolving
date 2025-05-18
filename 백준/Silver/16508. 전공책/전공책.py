from itertools import combinations
import sys

T = input()
N = int(input())

arr = []
for _ in range(N):
    a, b = input().split()
    arr.append([int(a), list(b)])

result = sys.maxsize
for i in range(1,N+1):
    for j in combinations(range(N), i):
        tempMoney = 0
        tempLst = []
        for k in list(j):
            tempMoney += arr[k][0]
            tempLst += arr[k][1]

        for t in list(T):
            if t in  tempLst:
                idx = tempLst.index(t)
                tempLst.pop(idx)
            else:
                break
        else:
            result = min(result, tempMoney)

if result == sys.maxsize:
    print(-1)
else:
    print(result)
