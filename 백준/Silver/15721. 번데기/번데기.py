def solve():
    if word == 0 and cnt0 == T:
        print(idx % A)
        exit(0)
    elif word == 1 and cnt1 == T:
        print(idx % A)
        exit(0)

A = int(input())
T = int(input())
word = int(input())

idx = 0
level = 1
cnt0 = 0
cnt1 = 0
while True:
    for i in range(4):
        if i % 2 == 0:
            cnt0 += 1
            solve()
        else:
            cnt1 += 1
            solve()
        idx += 1
    for _ in range(level+1):
        cnt0 += 1
        solve()
        idx += 1
    for _ in range(level+1):
        cnt1 += 1
        solve()
        idx += 1
    level += 1