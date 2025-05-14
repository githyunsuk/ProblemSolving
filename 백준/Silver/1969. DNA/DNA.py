N, M = map(int, input().split())
dna = [input() for _ in range(N)]

cnt = 0
result = ''
for i in range(M):
    lst = [0,0,0,0]
    for j in range(N):
        if dna[j][i] == 'A':
            lst[0] += 1
        elif dna[j][i] == 'C':
            lst[1] += 1
        elif dna[j][i] == 'G':
            lst[2] += 1
        elif dna[j][i] == 'T':
            lst[3] += 1
    idx = lst.index(max(lst))
    if idx == 0:
        result += 'A'
    elif idx == 1:
        result += 'C'
    elif idx == 2:
        result += 'G'
    elif idx == 3:
        result += 'T'
    cnt += N - max(lst)
print(result)
print(cnt)