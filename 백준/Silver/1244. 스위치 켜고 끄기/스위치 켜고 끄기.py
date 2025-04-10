N = int(input())
arr = [-1] + list(map(int, input().split()))
for _ in range(int(input())):
    a, b = map(int, input().split())
    if a == 1:
        for i in range(1, N//b + 1):
            if arr[i*b] == 0:
                arr[i*b] = 1
            else:
                arr[i*b] = 0
    else:
        if arr[b] == 0:
            arr[b] = 1
        else:
            arr[b] = 0
        left, right = b-1, b+1
        while left > 0 and right <= N and arr[left] == arr[right]:
            if arr[left] == 0:
                arr[left], arr[right] = 1, 1
            else:
                arr[left], arr[right] = 0, 0
            left -= 1
            right += 1

for i in range(1, N+1):
    print(arr[i], end=" ")
    if i % 20 == 0:
        print()