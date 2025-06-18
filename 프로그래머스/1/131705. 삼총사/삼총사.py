def solution(n):
    result = 0
    for i in range(len(n)-2):
        for j in range(i+1, len(n)-1):
            for k in range(j+1, len(n)):
                if n[i] + n[j] + n[k] == 0:
                    result += 1
    return result
                    