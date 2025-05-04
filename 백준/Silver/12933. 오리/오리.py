sound = input()
visited = [False] * len(sound)
quack = 'quack'
cnt = 0

if len(sound) % 5 != 0:
    print(-1)
    exit()

for i in range(len(sound)):
    idx = 0
    flag = True
    for j in range(i, len(sound)):
        if sound[j] == quack[idx] and visited[j] == False:
            visited[j] = True
            if quack[idx] == 'k':
                if flag:
                    cnt += 1
                    flag = False
                idx = 0
            else:
                idx += 1

if cnt == 0 or not all(visited):
    print(-1)
else:
    print(cnt)