n = int(input())
arr = list(map(int, input().split()))

result = []
for i in range(1, min(arr)+1):
    for a in arr:
        if a % i != 0:
            break

    else:
        print(i)