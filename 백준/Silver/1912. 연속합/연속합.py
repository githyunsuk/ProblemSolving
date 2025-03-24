N = int(input())
data = list(map(int, input().split()))

for i in range(1, N):
    data[i] = max(data[i], data[i] + data[i-1])
print(max(data))