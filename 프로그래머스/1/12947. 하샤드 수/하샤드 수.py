def solution(x):
    flag = False
    num = int(sum(map(int, str(x))))
    if x % num == 0:
        flag = True
    return flag