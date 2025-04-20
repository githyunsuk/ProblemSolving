N = int(input())
stars = [[' ' for _ in range(4 * N - 3)] for _ in range(4 * N - 3)]

def solve(n, di, dj):
    if n == 1:
        stars[di][dj] = '*'
        return
    length = 4 * n - 3

    for a in range(length):
        stars[di][dj+a] = '*'
        stars[di+a][dj] = '*'
        stars[di+length-1][dj+a] = '*'
        stars[di+a][dj+length-1] = '*'

    solve(n-1, di+2, dj+2)

solve(N, 0, 0)
for s in stars:
    print(''.join(s))