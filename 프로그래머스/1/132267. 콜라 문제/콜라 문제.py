def solution(a, b, n):
    result = 0  
    empty = n   
    
    while empty >= a:
        new = (empty // a) * b  
        result += new
        empty = (empty % a) + new 
    
    return result