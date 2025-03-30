money = int(input())
arr = list(map(int, input().split()))

result = 'BNP'

def bnf():
    total = 0
    remain = money
    for i in arr:
        if total == 0 and i <= remain:
            total += remain // i
            remain %= i
    return remain + arr[-1] * total


def timing():
    total = 0
    cntUp = 0
    cntDwn = 0
    remain = money
    for i in range(1, len(arr)):
        if arr[i] < arr[i-1]:
            cntDwn += 1
            cntUp = 0
        elif arr[i] > arr[i-1]:
            cntUp += 1
            cntDwn = 0

        if cntDwn >= 3 and arr[i] <= remain:
            total +=  remain // arr[i]
            remain %= arr[i]
        if cntUp == 3 and total > 0:
            return remain + total * arr[i]
    return remain + total * arr[-1]

if bnf() < timing():
    result = 'TIMING'
elif bnf() == timing():
    result = 'SAMESAME'
print(result)



