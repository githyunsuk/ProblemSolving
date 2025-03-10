N = input()
if len(N) == 1:
    N = '0' + N

temp = N
result = 0
while True:
    temp2 = str(int(N[0]) + int(N[1]))
    N= N[1] + temp2[-1]
    result += 1
    if N == temp:
        break
print(result)

