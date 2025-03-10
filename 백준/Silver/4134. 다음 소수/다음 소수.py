T = int(input())
for _ in range(T):
    n = int(input())

    if n < 2:
        print(2)
        continue
    while True:
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                break
        else:
            break
        n += 1

    print(n)