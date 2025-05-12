a, b, c, d, e, f = map(int, input().split())

def solve(x, y):
    if a * x + b * y == c and d * x + e * y == f:
        return True
    return False
for x in range(1000):
    for y in range(1000):
        if solve(x,y):
            print(x, y)
            exit(0)
        if solve(-x,y):
            print(-x, y)
            exit(0)
        if solve(x,-y):
            print(x, -y)
            exit(0)
        if solve(-x,-y):
            print(-x, -y)
            exit(0)