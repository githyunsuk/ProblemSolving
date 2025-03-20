n = int(input())
dp = [0] * (20 + 1)
dp[1] = 1

for i in range(2, len(dp)):
    dp[i] = dp[i-1] + dp[i-2]

print(dp[n])