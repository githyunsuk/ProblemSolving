data = input().split('-')

lst = list()
for d in data:
    temp = 0
    num = d.split('+')
    for i in num:
        temp += int(i)
    lst.append(temp)

result = lst[0]
for i in range(1, len(lst)):
    result -= lst[i]
print(result)