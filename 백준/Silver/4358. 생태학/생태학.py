import sys
input = sys.stdin.readline

dic = {}
total = 0
while True:
    word = input().rstrip()
    if word == '':
        break
    total += 1
    if word in dic:
        dic[word] += 1
    else:
        dic[word] = 1

sdic = dict(sorted(dic.items()))
for i in sdic:
    print(f'{i} {sdic[i] / total * 100:.4f}')