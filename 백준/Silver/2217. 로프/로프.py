import sys
input = sys.stdin.readline

n = int(input())
rope = []
for _ in range(n):
  rope.append(int(input()))

rope.sort()

result = []

for i in rope:
  result.append(i * n)
  n -= 1
print(max(result))