def solution(arr):
    result = []
    for a in arr:
        if len(result) == 0 or result[-1] != a:
            result.append(a)
    return result
