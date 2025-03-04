from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
q = deque()

for _ in range(N):
    com = input().rstrip().split()

    if com[0] == 'push_front':
        q.appendleft(com[1])
    if com[0] == 'push_back':
        q.append(com[1])
    if com[0] == 'pop_front':
        print(q.popleft()) if q else print(-1)
    if com[0] == 'pop_back':
        print(q.pop()) if q else print(-1)
    if com[0] == 'size':
        print(len(q))
    if com[0] == 'empty':
        print(0) if q else print(1)
    if com[0] == 'front':
        print(q[0]) if q else print(-1)
    if com[0] == 'back':
        print(q[-1]) if q else print(-1)