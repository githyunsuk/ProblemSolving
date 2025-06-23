def solution(n, m, section):
    result = 0
    painted = 0 

    for s in section:
        if s >= painted:  
            painted = s + m 
            result += 1

    return result