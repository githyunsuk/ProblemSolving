N = int(input())
distance = list(map(int, input().split()))
oil = list(map(int,input().split()))

total = oil[0] * distance[0]
min_cost = oil[0]

for i in range(1, N-1):
  if oil[i] < min_cost:
    min_cost = oil[i]
  total += min_cost * distance[i]

print(total)