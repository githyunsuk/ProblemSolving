N, M = map(int, input().split())

lst = [[] for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    lst[a].append(b)
    lst[b].append(a)

cnt = 0
result=[]
for i in range(1, N-1):
    for j in range(i+1, N):
        if j in lst[i]:
            continue
        for k in range(j+1, N+1):
            if k in lst[i] or k in lst[j]:
                continue
            cnt += 1
            
print(cnt)
