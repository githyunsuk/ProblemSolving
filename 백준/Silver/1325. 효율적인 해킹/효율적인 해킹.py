from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    graph[b].append(a)

def bfs(start):
    visited = [False] * (N + 1)
    queue = deque([start])
    visited[start] = True
    cnt = 1

    while queue:
        v = queue.popleft()
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
                cnt += 1
    return cnt

result = [0] * (N+1)
maxCount = 0

for i in range(1, N+1):
    result[i] = bfs(i)
    maxCount = max(maxCount, result[i])

for i in range(1, N+1):
    if result[i] == maxCount:
        print(i, end=' ')
