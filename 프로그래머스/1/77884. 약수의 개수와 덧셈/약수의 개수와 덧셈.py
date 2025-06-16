def solution(left, right):
    result = 0
    for i in range(left, right + 1):
        # 약수의 개수 구하기
        cnt = 0
        for j in range(1, int(i ** 0.5) + 1):
            if i % j == 0:
                if j == i // j:
                    cnt += 1
                else:
                    cnt += 2
        if cnt % 2 == 0:
            result += i
        else:
            result -= i
    return result
   