import sys
from collections import deque
input = sys.stdin.readline

n, m, v = map(int,input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in graph:
    i.sort()
visited = [False] * (n+1)

def dfs(v):
    visited[v] = True
    print(v, end=' ')
    for i in graph[v]:
        if not visited[i]:
            dfs(i)

def bfs(v):
    queue = deque([v])
    visited[v] = True
    while queue:
        node = queue.popleft()
        print(node, end=' ')
        for i in graph[node]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

dfs(v)
print()
visited = [False] * (n+1)
bfs(v)

