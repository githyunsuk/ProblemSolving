N, B = input().split()
N = N[::-1]
B = int(B)

number = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
result = 0

for i, n in enumerate(N):
    result += (B ** i) * (number.index(n))

print(result)
