N = int(input())

dic = {}
result = 0
for i in range(N):
    a, b = map(int, input().split())
    if a in dic:
        if dic[a] != b:
            dic[a] = b
            result += 1
    else:
        dic[a] = b
print(result)
