def solution(array, commands):
    result = []
    for c in commands:
        i, j, k = c
        result.append(sorted(array[i-1 : j])[k-1])
    return result