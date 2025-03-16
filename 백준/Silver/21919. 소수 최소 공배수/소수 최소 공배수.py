def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a%b)

prime = [True] * 1000001
prime[0] = prime[1] = False

for i in range(2, int(len(prime) ** 0.5) + 1):
    for j in range(i+i, len(prime), i):
        if prime[j]:
            prime[j] = False

result = 1
N = int(input())
A = list(map(int, input().split()))
temp = []
for i in A:
    if prime[i]:
        temp.append(i)

if not temp:
    print(-1)
else:
    result = temp[0]
    for i in range(1, len(temp)):
        result = result * temp[i] // gcd(result, temp[i])
    print(result)
