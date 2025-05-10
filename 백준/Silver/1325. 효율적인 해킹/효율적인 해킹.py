from collections import deque

N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    graph[b].append(a)

visited = [False] * (N+1)
def bfs(start):
    queue = deque([start])
    visited[start] = True

    while queue:
        v = queue.popleft()
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

result = [0] * (N+1)
for i in range(1, N+1):
    if graph[i]:
        bfs(i)
        result[i] = visited.count(True)
        visited = [False] * (N+1)

mxValue = max(result)
for i in range(1, N+1):
    if result[i] == mxValue:
        print(i, end=' ')
