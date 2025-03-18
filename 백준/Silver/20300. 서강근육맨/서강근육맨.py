import sys
input = sys.stdin.readline

N = int(input())
arr = sorted(list(map(int, input().split())))

result = 0
if len(arr) % 2 == 0:
    for i in range(len(arr)//2):
        result = max(result, arr[i] + arr[len(arr)-i-1])
    print(result)

else:
    for i in range(len(arr)//2):
        result = max(result, arr[i] + arr[len(arr)-i-2])
    print(max(result, arr[-1]))
