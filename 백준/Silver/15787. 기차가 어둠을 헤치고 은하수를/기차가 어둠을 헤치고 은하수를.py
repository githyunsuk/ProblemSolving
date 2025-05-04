n, m = map(int, input().split())
train = [[0 for _ in range(20)] for _ in range(n)]

for _ in range(m):
    data = list(map(int, input().split()))
    command = data[0]
    i = data[1] - 1

    if command == 1:
        x = data[2] - 1
        train[i][x] = 1

    elif command == 2:
        x = data[2] - 1
        train[i][x] = 0

    elif command == 3:
        for j in range(19, 0, -1):
            train[i][j] = train[i][j - 1]
        train[i][0] = 0

    elif command == 4:
        for j in range(19):
            train[i][j] = train[i][j + 1]
        train[i][19] = 0

result = []
for i in range(n):
    if train[i] not in result:
        result.append(train[i])

print(len(result))
