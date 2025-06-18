def solution(s):
    answer = ''
    arr = s.split(" ")
    for a in arr:
        for i in range(len(a)):
            if i%2 == 0:
                answer += a[i].upper()
            else:
                answer += a[i].lower()
        answer += ' '
    
    return answer[:-1]