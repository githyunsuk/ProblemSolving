left = [['q', 'w', 'e', 'r', 't'],
        ['a','s','d','f','g'],
        ['z','x','c','v',0]]
right = [[0,'y','u','i','o','p'],
         [0,'h','j','k','l',0],
         ['b','n','m',0,0,0]]

sl, sr = input().split()
word = list(input())

# 시작 위치 찾기
for i in range(3):
    for j in range(5):
        if left[i][j] == sl:
            li, lj = i, j
for i in range(3):
    for j in range(6):
        if right[i][j] == sr:
            ri, rj = i, j

result = 0
for ch in word:
    if any(ch in row for row in left):  # 왼손 자판이면
        for i in range(3):
            for j in range(5):
                if left[i][j] == ch:
                    ti, tj = i, j
                    break
        result += abs(li - ti) + abs(lj - tj) + 1
        li, lj = ti, tj
    else:  # 오른손 자판이면
        for i in range(3):
            for j in range(6):
                if right[i][j] == ch:
                    ti, tj = i, j
                    break
        result += abs(ri - ti) + abs(rj - tj) + 1
        ri, rj = ti, tj

print(result)
