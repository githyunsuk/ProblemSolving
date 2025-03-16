import sys
input = sys.stdin.readline

N = int(input())
arr = [int(input()) for _ in range(N)]
arr.sort(reverse=True)

temp = []
result = 0
for i in range(len(arr)):
    temp.append(arr[i])
    if len(temp) == 3:
        result += (sum(temp) - min(temp))
        temp = []
    elif i == len(arr)-1:
        result += sum(temp)

print(result)