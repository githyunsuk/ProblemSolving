h, w = map(int, input().split())
N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

result = 0
for i in range(N):
    for j in range(i+1, N):
        r1, c1 = arr[i]
        r2, c2 = arr[j]

        if (r1 + r2 <= h and max(c1, c2) <= w) or (max(r1, r2) <= h and c1 + c2 <= w):
            result = max(result, r1 * c1 + r2 * c2)
        if (c1 + r2 <= h and max(r1, c2) <= w) or (max(c1, r2) <= h and r1 + c2 <= w):
            result = max(result, r1 * c1 + r2 * c2)
        if (c1 + c2 <= h and max(r1, r2) <= w) or (max(c1, c2) <= h and r1 + r2 <= w):
            result = max(result, r1 * c1 + r2 * c2)
        if (r1 + c2 <= h and max(c1, r2) <= w) or (max(r1, c2) <= h and c1 + r2 <= w):
            result = max(result, r1 * c1 + r2 * c2)

print(result)
