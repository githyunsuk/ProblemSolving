def solution(price, money, count):
    
    total = 0
    for i in range(1, count+1):
        total += price * i
    
    result = total - money
    return 0 if result <= 0 else result