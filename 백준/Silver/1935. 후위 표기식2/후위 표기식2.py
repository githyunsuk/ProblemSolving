N = int(input())
arr = input()
oper = "+-*/"
dic = {}
stack = []
num = []
for i in range(N):
    num.append(int(input()))
    
for i in arr:
    if i not in dic and i not in oper:
        dic[i] = num.pop(0)

for i in arr:
    if i not in oper:
        stack.append(dic[i])
    else:
        if i == '+':
            a = stack.pop()
            b = stack.pop()
            stack.append(b + a)
        elif i == '-':
            a = stack.pop()
            b = stack.pop()
            stack.append(b - a)
        elif i == '*':
            a = stack.pop()
            b = stack.pop()
            stack.append(b * a)
        else:
            a = stack.pop()
            b = stack.pop()
            stack.append(b / a)

print(f'{stack[0]:.2f}')