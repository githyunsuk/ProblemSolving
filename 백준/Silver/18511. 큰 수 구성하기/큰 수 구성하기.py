from itertools import product

N, K = map(int, input().split())
arr = list(map(int, input().split()))
length = len(str(N))

while True:
    tempArr = list(product(arr, repeat=length))
    result = []

    for t in tempArr:
        temp = int(''.join(map(str,t)))
        if temp <= N:
            result.append(temp)
    if result:
        print(max(result))
        break
    else:
        length -= 1