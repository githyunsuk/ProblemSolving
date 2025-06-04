N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

result = 0
for i in range(123, 988):
    num = str(i)
    if '0' in num or len(set(num)) != 3:
        continue
    cnt = 0
    for j in range(N):
        temp = str(arr[j][0])
        strike = 0
        ball = 0
        for k in range(3):
            if num[k] in temp:
                if num[k] == temp[k]:
                    strike += 1
                else:
                    ball += 1
        if strike == arr[j][1] and ball == arr[j][2]:
            cnt += 1
    if cnt == N:
        result += 1

print(result)
