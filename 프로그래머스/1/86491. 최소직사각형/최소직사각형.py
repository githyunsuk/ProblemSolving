def solution(sizes):
    a, b = 0, 0
    for s in sizes:
        s.sort()
        a = max(a, s[0])
        b = max(b, s[1])
    return a * b