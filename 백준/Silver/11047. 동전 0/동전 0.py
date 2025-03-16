N, K = map(int, input().split())
data = [int(input()) for _ in range(N)]
data.sort(reverse=True)

result = 0
for d in data:
    result += (K // d)
    K %= d
print(result)