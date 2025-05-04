data = input()

stack = []
result = ''
flag = False
for d in data:
    if d == '<':
        flag = True
        for _ in range(len(stack)):
            result += stack.pop()

    stack.append(d)

    if d == '>':
        flag = False
        for _ in range(len(stack)):
            result += stack.pop(0)

    if d == ' ' and flag == False:
        for i in range(len(stack)):
            if i == 0:
                stack.pop()
                continue
            result += stack.pop()
        result += ' '
if stack:
    for _ in range(len(stack)):
        result += stack.pop()

print(result)
