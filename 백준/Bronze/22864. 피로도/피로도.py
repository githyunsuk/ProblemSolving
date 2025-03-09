a, b, c, m = map(int, input().split())
tired = 0
work = 0

for i in range(24):
  if a > m:
    break
  else:
    if tired + a <= m:
      work += b
      tired += a
    else:
      if tired - c >= 0:
        tired -= c
      else:
        tired = 0

print(work)

   