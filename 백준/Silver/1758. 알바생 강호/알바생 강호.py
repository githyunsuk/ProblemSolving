import sys
input = sys.stdin.readline

N = int(input())
arr = sorted([int(input()) for _ in range(N)])
arr.sort(reverse=True)

idx = 1
result = 0
for i in arr:
    money = i - (idx-1)
    if money < 0:
        money = 0
    result += money
    idx += 1

print(result)
