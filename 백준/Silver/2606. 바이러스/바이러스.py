import sys
input = sys.stdin.readline

com = int(input())
num = int(input())

graph = [[] for _ in range(com+1)]
visited = [False] * (com+1)
for _ in range(num):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs(x):
    global count
    visited[x] = True
    count += 1
    for i in graph[x]:
        if not visited[i]:
            dfs(i)
count = 0
dfs(1)
print(count-1)