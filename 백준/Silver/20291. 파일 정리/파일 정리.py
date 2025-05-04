N = int(input())

dic = {}
for _ in range(N):
    file = input()
    idx = file.find('.')
    word = file[idx+1:]
    if word in dic:
        dic[word] += 1
    else:
        dic[word] = 1

dic = dict(sorted(dic.items()))
items = list(dic.items())

for i in range(len(dic)):
    print(items[i][0] + " " + str(items[i][1]))