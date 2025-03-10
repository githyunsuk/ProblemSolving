def gcd(a, b):
    if a < b:
        a, b = b, a
    while b > 0:
        a, b = b, a % b
    return a

N = int(input())
arr = list(map(int, input().split()))
X = int(input())
result = []

for a in arr:
    if gcd(a, X) == 1:
        result.append(a)

print(sum(result) / len(result))
