def solution(s):
    arr = []
    dic = dict()
    for i in range(len(s)):
        if s[i] not in dic:
            arr.append(-1)
        else:
            arr.append(i-dic[s[i]])
        dic[s[i]] = i
    return arr