def solution(word, n):
    result = ''
    for w in word:
        if w == ' ':
            result += ' '
        elif 'a' <= w <= 'z':
            result += chr((ord(w) - ord('a') + n) % 26 + ord('a'))
        elif 'A' <= w <= 'Z':
            result += chr((ord(w) - ord('A') + n) % 26 + ord('A'))
    return result