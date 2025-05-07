def solve(graph, n, d):
    for _ in range(abs(d) // 45):
        mainDiag = [graph[i][i] for i in range(n)]
        subDiag = [graph[n-1-i][i] for i in range(n)]
        row = [graph[n//2][i] for i in range(n)]
        column = [graph[i][n//2] for i in range(n)]

        if d > 0:
            for i in range(n):
                graph[i][i] = row[i]
                graph[i][n - 1 - i] = column[i]
                graph[n//2][i] = subDiag[i]
                graph[i][n//2] = mainDiag[i]
        else:
            for i in range(n):
                graph[i][i] = column[i]
                graph[n-1-i][i] = row[i]
                graph[n // 2][i] = mainDiag[i]
                graph[n-1-i][n // 2] = subDiag[i]


for _ in range(int(input())):
    N, D = map(int ,input().split())
    graph = [list(map(int, input().split())) for _ in range(N)]
    solve(graph, N, D)
    for g in graph:
        print(*g)

