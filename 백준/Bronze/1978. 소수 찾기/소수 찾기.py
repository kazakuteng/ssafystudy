def iscoprime(numm):
    check = True
    if numm == 1:
        check = False
    for i in range(2, numm//2+1):
        if numm % i == 0:
            check = False
            break
    return check

N=int(input())
a = list(map(int, input().split()))
total = 0
for i in a:
    if iscoprime(i):
        total += 1
print(total)