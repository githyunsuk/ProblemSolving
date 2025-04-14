N = int(input())
arr1 = [list(input()) for _ in range(N)]
arr2 = [list(input()) for _ in range(N)]

di = [-1,1,0,0,-1,-1,1,1]
dj = [0,0,1,-1,-1,1,-1,1]

isMine = False
for i in range(N):
    for j in range(N):
        if arr2[i][j] == 'x':
            if arr1[i][j] == '*':
                isMine = True
            cnt = 0
            for k in range(8):
                ni = i + di[k]
                nj = j + dj[k]
                if ni<0 or nj<0 or ni>=N or nj>=N:
                    continue
                if arr1[ni][nj] == '*':
                    cnt += 1
            arr2[i][j] = str(cnt)

if isMine:
    for i in range(N):
        for j in range(N):
            if arr1[i][j] == '*':
                arr2[i][j] = '*'


for a in arr2:
    print(''.join(a))

