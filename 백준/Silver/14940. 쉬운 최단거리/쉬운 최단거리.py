from collections import deque

width, length = map(int, input().split())
graph = [list(map(int,input().split())) for _ in range(width)]

dx = [-1,1,0,0]
dy = [0,0,-1,1]
visited = [[-1] * length for _ in range(width)]

def bfs(x,y):
    queue = deque()
    queue.append((x,y))
    visited[x][y] = 0

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx<0 or ny<0 or nx>=width or ny>=length:
                continue
            if visited[nx][ny] == -1:
                if graph[nx][ny] == 0:
                    visited[nx][ny] = 0
                elif graph[nx][ny] == 1:
                    queue.append((nx, ny))
                    visited[nx][ny] = visited[x][y] + 1

for x in range(width):
    for y in range(length):
        if graph[x][y] == 2 and visited[x][y] == -1:
            bfs(x,y)

for i in range(width):
    for j in range(length):
        if graph[i][j] == 0:
            print(0, end=' ')
        else:
            print(visited[i][j], end=' ')
    print()