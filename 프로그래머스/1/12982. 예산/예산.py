def solution(data, budget):
    result = 0
    data.sort()
    for d in data:
        budget -= d
        if budget < 0:
            break
        result += 1
    return result