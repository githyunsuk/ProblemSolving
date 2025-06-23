def solution(answers):
    s1 = [1,2,3,4,5]
    s2 = [2,1,2,3,2,4,2,5]
    s3 = [3,3,1,1,2,2,4,4,5,5]
    result = []
    
    c1, c2, c3 = 0, 0, 0
    for i in range(len(answers)):
        if answers[i] == s1[i % len(s1)]:
            c1 += 1
        if answers[i] == s2[i % len(s2)]:
            c2 += 1
        if answers[i] == s3[i % len(s3)]:
            c3 += 1
    mx = max(c1,c2,c3)
    
    if mx == c1:
        result.append(1)
    if mx == c2:
        result.append(2)
    if mx == c3:
        result.append(3)
    return result
        
            
            
            