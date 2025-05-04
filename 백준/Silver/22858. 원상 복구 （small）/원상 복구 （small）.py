N, K = map(int, input().split())
S = list(map(int, input().split()))
D = list(map(int, input().split()))

for _ in range(K):
    idx = 0
    tempList = [0] * N
    for d in D:
        tempList[d-1] = S[idx]
        idx += 1
    S = tempList

print(*S)