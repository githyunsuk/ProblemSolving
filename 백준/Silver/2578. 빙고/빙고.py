def solve(n):
    for i in range(5):
        for j in range(5):
            if bingo[i][j] == n:
                bingo[i][j] = 0

    result = 0
    bingo_t = list(zip(*bingo))
    for lst in bingo:
        if sum(lst) == 0:
            result += 1
    for lst in bingo_t:
        if sum(lst) == 0:
            result += 1
    for i in range(5):
        if bingo[i][i] != 0:
            break
    else:
        result += 1
    for i in range(5):
        if bingo[i][4-i] != 0:
            break
    else:
            result += 1
    return result
bingo = [list(map(int, input().split())) for _ in range(5)]
arr = [list(map(int, input().split())) for _ in range(5)]

cnt = 0
for lst in arr:
    for l in lst:
        cnt += 1
        if solve(l) >= 3:
            print(cnt)
            exit(0)