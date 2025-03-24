dp = [[0] * 101 for _ in range(101)]

for i in range(1, len(dp)):
    dp[1][i] = i
for i in range(2, len(dp)):
    for j in range(i, len(dp)):
        dp[i][j] = dp[i-1][j-1] + dp[i][j-1]

N, M = map(int, input().split())
print(dp[M][N])