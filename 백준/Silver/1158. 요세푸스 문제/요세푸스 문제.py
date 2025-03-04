import sys
input = sys.stdin.readline

n, k = map(int, input().split())

array = list(range(1,n+1))
result = []
idx = 0

while array:
  idx += k - 1
  idx %= len(array)
  result.append(array.pop(idx))

print("<", end="")
print(', '.join(map(str,result)), end="")
print(">")