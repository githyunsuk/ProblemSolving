import sys
input = sys.stdin.readline

def gcd(a,b):
    if b == 0:
        return a
    return gcd(b, a%b)

T = int(input())
for _ in range(T):
    arr = list(map(int, input().split()))

    result = 0
    for i in range(1, len(arr)):
        for j in range(i+1, len(arr)):
            result += gcd(arr[i],arr[j])
    print(result)