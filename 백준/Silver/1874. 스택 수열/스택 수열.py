import sys
input = sys.stdin.readline

N = int(input())
stack = [int(input()) for _ in range(N)]
stack2 = []
result = []

cur = 1
for num in stack:
    while cur <= num:
        stack2.append(cur)
        result.append('+')
        cur += 1
    if stack2[-1] == num:
        stack2.pop()
        result.append('-')
    else:
        print("NO")
        exit()

print("\n".join(result))