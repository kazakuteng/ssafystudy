N, M = map(int, input().split())
arr = []
for i in range(N):
    arr.append(int(input()))
minn = 0
maxx = 10**18

while minn<=maxx:
    
    middle = (minn + maxx)//2
    
    total = 0
    for i in arr:
        total += middle // i
    if total < M:
        minn = middle + 1
    else:
        maxx = middle - 1

print(minn)