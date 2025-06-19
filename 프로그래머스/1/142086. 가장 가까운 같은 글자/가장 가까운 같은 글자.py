def solution(s):
    arr = [-1] * len(s)
    for i in range(1, len(s)):
        for j in range(i-1, -1, -1):
            if s[i] == s[j]:
                arr[i] = i - j
                break
    return arr
            