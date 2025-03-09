import heapq

N = int(input())
hq = []
for i in range(N):
    arr = list(map(int, input().split()))
    if not hq:
        for a in arr:
            heapq.heappush(hq, a)
    else:
        for a in arr:
            if hq[0] < a:
                heapq.heappush(hq,a)
                heapq.heappop(hq)

print(hq[0])
