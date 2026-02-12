N, M = map(int, input().split())
arr= []
for i in range(N):
    arr.append(int(input()))

minn = max(arr)
maxx = minn * N

while minn <= maxx:
    total = 0
    middle = (minn + maxx) // 2
    cur = 0
    for i in arr:
        if cur < i:
            total += 1
            cur = middle - i
        else:
            cur -= i


    if M < total:
        minn = middle + 1

    else:
        maxx = middle - 1
print(minn)