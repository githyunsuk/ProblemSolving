word = input()

maxValue = ""
minValue = ""
m = 0
for i in range(len(word)):
    if word[i] == 'M':
        m += 1
    elif word[i] == 'K':
        if m:
            minValue += str(10**m + 5)
            maxValue += str((10**m) * 5)
        else:
            minValue += "5"
            maxValue += "5"
        m = 0

if m:
    minValue += str(10 ** (m-1))
    for i in range(m):
        maxValue += '1'
print(maxValue)
print(minValue)