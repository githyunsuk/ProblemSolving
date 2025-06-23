def solution(answers):
    s1 = [1,2,3,4,5]
    s2 = [2,1,2,3,2,4,2,5]
    s3 = [3,3,1,1,2,2,4,4,5,5]
    result = []
    c = [0,0,0]
    
    for i in range(len(answers)):
        if answers[i] == s1[i % len(s1)]:
            c[0] += 1
        if answers[i] == s2[i % len(s2)]:
            c[1] += 1
        if answers[i] == s3[i % len(s3)]:
            c[2] += 1
    
    for idx, s in enumerate(c):
        if s == max(c):
            result.append(idx+1)

    return result
        
            
            
            