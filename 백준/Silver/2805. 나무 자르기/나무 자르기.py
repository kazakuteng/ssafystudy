
N, M = map(int, input().split())
number = list(map(int, input().split()))

minn = 0
maxx = max(number)
while minn <= maxx:
    middle = (maxx + minn) //2 
    total = 0
    for i in number:
        total += max(i -middle,0)

    if total < M:
        maxx = middle - 1

    else:
        minn = middle + 1
print(maxx)