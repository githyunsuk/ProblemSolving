from itertools import combinations

def solution(nums):
    answer = 0
    
    for a, b, c in combinations(nums, 3):
        temp = a + b + c
        for i in range(2, int(temp ** 0.5) + 1):
            if temp % i == 0:
                break
        else:
            answer += 1
                

    return answer