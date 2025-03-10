def gcd(a,b):
    if a < b:
        a,b = b,a
    while b > 0:
        a, b = b, a%b
    return a

N = int(input())
for _ in range(N):
    a, b = map(int, input().split())
    print(a*b // gcd(a,b))