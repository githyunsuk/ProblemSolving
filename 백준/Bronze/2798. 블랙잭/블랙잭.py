N, M = map(int, input().split())
arr = list(map(int, input().split()))

ans = 0
for i in range(0, N-2):
    for j in range(i+1, N-1):
        for k in range(j+1, N):
            temp = arr[i] + arr[j] + arr[k]
            if ans < temp <= M:
                ans = temp

print(ans)