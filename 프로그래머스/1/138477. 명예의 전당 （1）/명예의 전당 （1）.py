def solution(k, score):
    temp = []
    result = []
    for s in score:
        temp.append(s)
        if (len(temp) > k):
            temp.remove(min(temp))
        result.append(min(temp))

    return result