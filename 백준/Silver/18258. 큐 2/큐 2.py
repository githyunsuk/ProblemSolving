from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
queue = deque()

for i in range(N):
    command = input().split()

    if command[0] == "push":
        queue.append(command[1])
    if command[0] == "pop":
        print(queue.popleft()) if queue else print(-1)
    if command[0] == "size":
        print(len(queue))
    if command[0] == "empty":
        print(0) if queue else print(1)
    if command[0] == "front":
        print(queue[0]) if queue else print(-1)
    if command[0] == "back":
        print(queue[-1]) if queue else print(-1)

