def solution(n):
    arr = [True for i in range(n+1)]
    
    for i in range(2, int(n ** 0.5) + 1):
        if arr[i] == True:
            j = 2
            while i * j <= n:
                arr[i * j] = False
                j += 1
    return arr[2:].count(True)