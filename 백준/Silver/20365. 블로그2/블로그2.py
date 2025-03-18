import sys
input = sys.stdin.readline

N = int(input())
word = input().rstrip()

cnt1 = 1
group = False
for i in word:
    if i == 'B':
        if not group:
            cnt1 += 1
            group = True
    else:
        group = False

cnt2 = 1
group = False
for j in word:
    if j == 'R':
        if not group:
            cnt2 += 1
            group = True
    else:
        group = False

print(min(cnt1, cnt2))