from collections import deque

N = int(input())
lst = list(map(int, input().split()))
q = deque(range(1, N+1))
result = []

while q:
    tmp = q.popleft()
    result.append(tmp)
    if lst[tmp-1] > 0:
        q.rotate(-(lst[tmp-1]-1))
    else:
        q.rotate(-lst[tmp-1])


print(*result)