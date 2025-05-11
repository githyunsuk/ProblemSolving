
N = int(input())
graph = [list(map(int, input())) for _ in range(N)]

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def dfs(x,y):
    if x<0 or y<0 or x>=N or y>=N or graph[x][y]==0:
        return False

    global count
    count += 1
    graph[x][y] = 0
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        dfs(nx,ny)
    return True

result = []
for i in range(N):
    for j in range(N):
        if graph[i][j] != 0:
            count = 0
            dfs(i,j)
            result.append(count)
result.sort()
print(len(result))
for r in result:
    print(r)