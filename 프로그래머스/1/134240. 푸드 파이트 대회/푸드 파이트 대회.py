def solution(food):
    result = ''
    for i in range(1, len(food)):
        result += str(i) * (food[i] // 2)
    result += '0'
    for i in range(len(food)-1, 0, -1):
        result += str(i) * (food[i] // 2)
    return result