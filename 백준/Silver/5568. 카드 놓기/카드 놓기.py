from itertools import permutations

N = int(input())
K = int(input())
lst = [input() for _ in range(N)]

result = set()
for p in permutations(lst,K):
    num = ''.join(p)
    result.add(num)

print(len(result))
