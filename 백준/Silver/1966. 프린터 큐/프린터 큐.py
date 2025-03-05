import sys
input = sys.stdin.readline

n = int(input())

for _ in range(n):
  a, b = map(int, input().split())
  priority = list(map(int, input().split()))
  idx_list = list(range(0, a))

  count = 0
  while True:
    if priority[0] == max(priority):
      count += 1

      if idx_list[0] == b:
        print(count)
        break

      else:
        del priority[0]
        del idx_list[0]
    else:
      priority.append(priority.pop(0))
      idx_list.append(idx_list.pop(0))