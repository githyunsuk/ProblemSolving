from itertools import combinations

def solution(numbers):
    arr = set()
    for a, b in combinations(numbers, 2):
        arr.add(a+b)
    return sorted(list(arr))