import sys
input = sys.stdin.readline

N = int(input())
F = int(input())

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]
arr = [[0] * N for _ in range(N)]
r, c = N // 2, N //2
arr[r][c] = 1
num = 1
length = 0
rr, rc = r+1, c+1

while True:
    for i in range(4):
        for j in range(length):
            r += dr[i]
            c += dc[i]
            num += 1
            arr[r][c] = num
            if num == F:
                rr, rc = r+1, c+1
    if r == c == 0:
        break
    r -= 1
    c -= 1
    length += 2

for a in arr:
    print(*a)
print(rr, rc)

