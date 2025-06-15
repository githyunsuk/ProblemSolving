def solution(s):
    flag = False
    s = s.lower()
    
    if s.count('p') == s.count('y'):
        flag = True

    return flag