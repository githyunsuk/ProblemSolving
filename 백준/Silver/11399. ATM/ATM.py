N = int(input())
data = sorted(list(map(int, input().split())))

result = 0
for i in range(len(data)):
    result += sum(data[:i+1])
print(result)