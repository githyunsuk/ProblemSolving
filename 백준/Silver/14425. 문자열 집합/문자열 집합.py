import sys
input = sys.stdin.readline

N, M = map(int, input().split())
dic = {input().rstrip() for _ in range(N)}

result = 0
for _ in range(M):
    tmp = input().rstrip()
    if tmp in dic:
        result += 1

print(result)