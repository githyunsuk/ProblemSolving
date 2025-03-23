dp = [[0 for _ in range(31)] for _ in range(31)]
for i in range(1, 31):
    dp[1][i] = i

for i in range(2, 31):
    for j in range(i, 31):
        dp[i][j] = dp[i-1][j-1] + dp[i][j-1]

for _ in range(int(input())):
    N, M = map(int, input().split())
    print(dp[N][M])

