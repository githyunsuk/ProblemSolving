def solve(i, j):
    temp[i][j] = '.'

    for k in range(4):
        ni = i + di[k]
        nj = j + dj[k]

        if 0<=ni<R and 0<=nj<C:
            temp[ni][nj] = '.'

R, C, N = map(int, input().split())
board = [list(input()) for _ in range(R)]
time = 1

di = [-1,1,0,0]
dj = [0,0,-1,1]

if N % 2 == 0:
    for _ in range(R):
        print('O' * C)
    exit(0)

while time < N:
    temp = [['O'] * C for _ in range(R)]
    for i in range(R):
        for j in range(C):
            if board[i][j] == 'O':
                solve(i, j)
    board = temp
    time += 2

for b in board:
    print(''.join(b))