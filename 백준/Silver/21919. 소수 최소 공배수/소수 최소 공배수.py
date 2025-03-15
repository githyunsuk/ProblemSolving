def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a%b)

arr = [0] * 1000001
for i in range(2, int(len(arr)**0.5)+1):
    for j in range(i+i, len(arr), i):
        if arr[j] == 0:
            arr[j] = 1
arr[0] = 1
arr[1] = 1


result = 1
N = int(input())
A = list(map(int, input().split()))
temp = []
for i in A:
    if not arr[i]:
        temp.append(i)

if not temp:
    print(-1)
else:
    result = temp[0]
    for i in range(1, len(temp)):
        result = result * temp[i] // gcd(result, temp[i])
    print(result)