import sys
input = sys.stdin.readline

N = int(input())
stack = []
for _ in range(N):
    word = input().split()
    command = word[0]

    if command == "push":
        stack.append(int(word[1]))
    elif command == "pop":
        print(stack.pop()) if stack else print(-1)
    elif command == "size":
        print(len(stack))
    elif command == "empty":
        print(0) if stack else print(1)
    elif command == "top":
        print(stack[-1]) if stack else print(-1)