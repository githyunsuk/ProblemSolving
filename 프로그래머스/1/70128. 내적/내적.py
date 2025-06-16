def solution(aa, bb):
    result = 0
    for a, b in zip(aa, bb):
        result += a * b
    return result