N = int(input())
lst = list(map(int, input().split()))

cnt = 0
for l in lst:
    if l == 1:
        continue
    
    for i in range(2, int(l ** 0.5)+1):
        if (l % i) == 0:
            break
    else:
        cnt += 1
print(cnt)