import sys, heapq
input = sys.stdin.readline

hq = list()
N = int(input())
for _ in range(N):
    temp = int(input())
    if temp == 0:
        if hq:
            print(heapq.heappop(hq)[1])
        else:
            print(0)
    else:
        heapq.heappush(hq, (abs(temp), temp))
