def solution(arr, divisor):
    result = []
    for a in arr:
        if a % divisor == 0:
            result.append(a)
    return sorted(result) if result else [-1]