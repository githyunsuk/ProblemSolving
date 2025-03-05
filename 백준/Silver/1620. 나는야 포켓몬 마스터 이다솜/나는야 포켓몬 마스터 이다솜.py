import sys
input = sys.stdin.readline

n, m = map(int, input().split())

pokemon = {}
for i in range(1,n+1):
  name = input().rstrip()
  pokemon[i] = name
  pokemon[name] = i

for _ in range(m):
  a = input().rstrip()
  if a.isdigit():
    print(pokemon[int(a)])
  else:
    print(pokemon[a])