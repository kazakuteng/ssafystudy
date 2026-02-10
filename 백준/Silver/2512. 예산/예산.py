N = int(input())
number = list(map(int, input().split()))
M = int(input())
minn = 0
maxx = max(number)
while minn <= maxx:
    middle = (maxx + minn) //2 
    total = 0
    for i in number:
        total += min(i, middle)

    if total > M:
        maxx = middle - 1

    else:
        minn = middle + 1
print(maxx)