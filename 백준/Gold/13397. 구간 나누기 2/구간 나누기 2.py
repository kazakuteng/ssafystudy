N, M = map(int,input().split())
A = list(map(int,input().split()))

for i in range(0, 10000):
    total = 1
    minn = 10000
    maxx = 0
    for j in A:
        if maxx - i <= j <= minn + i:
            minn = min(j, minn)
            maxx = max(j, maxx)
        else:
            total += 1
            minn = j
            maxx = j
    if total <= M:
        print(i)
        break