import sys, heapq

input = sys.stdin.readline
N = int(input())
hq = list()
for _ in range(N):
    temp = int(input())
    if temp == 0:
        if hq:
            print(-heapq.heappop(hq))
        else:
            print(0)
    else:
        heapq.heappush(hq, -temp)