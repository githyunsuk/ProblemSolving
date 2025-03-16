import sys
input = sys.stdin.readline

N = int(input())
arr = sorted([int(input()) for _ in range(N)])

result = 0
for i in range(len(arr)):
    weight = arr[i] * (len(arr)-i)
    result = max(result, weight)

print(result)

