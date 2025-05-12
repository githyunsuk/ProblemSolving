N = int(input())

for i in range(1, N):
    num = sum(map(int, str(i)))
    if num + i == N:
        print(i)
        break
else:
    print(0)