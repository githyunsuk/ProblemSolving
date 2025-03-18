import sys
input = sys.stdin.readline

N = int(input())
word = input().rstrip()

rWord = [i for i in word.split('B') if i]
bWord = [i for i in word.split('R') if i]

result = min(len(rWord), len(bWord))
print(result + 1) 