def solution(k, score):
    temp = []
    result = []
    for s in score:
        if len(temp) < k:
            temp.append(s)
        else:
            if s > min(temp):
                temp.remove(min(temp))
                temp.append(s)
        result.append(min(temp))
    return result