N = 19
board = [list(map(int, input().split())) for _ in range(N)]

di = [0,1,1,-1]
dj = [1,0,1,1]
for i in range(N):
    for j in range(N):
        if board[i][j] != 0:
            for k in range(4):
                cnt = 1
                ni, nj = i, j
                while True:
                    ni += di[k]
                    nj += dj[k]
                    if 0<=ni<N and 0<=nj<N and board[ni][nj] == board[i][j]:
                        cnt += 1
                    else:
                        break
                    if cnt == 5:
                        if 0<=i-di[k]<N and 0<=j-dj[k]<N and board[i-di[k]][j-dj[k]] == board[i][j]:
                            break
                        if 0<=ni+di[k]<N and 0<=nj+dj[k]<N and board[ni+di[k]][nj+dj[k]] == board[i][j]:
                            break
                        print(board[i][j])
                        print(i+1, j+1)
                        exit(0)
print(0)