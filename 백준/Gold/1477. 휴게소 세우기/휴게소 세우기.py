N, M, L = map(int, input().split())
rest = list(map(int, input().split()))
rest.sort()
heap = [] 
for i in range(len(rest)+1): 
    if N == 0:
        heap.append(L)
    else:
        if i == 0: 
            heap.append(rest[i]) 
        elif i == len(rest): 
            heap.append(L - rest[i-1]) 
        else: 
            heap.append(rest[i] - rest[i-1])
minn = 1
maxx = L

while minn<=maxx:
    middle = (minn + maxx)//2
    total = 0
    for i in heap:
        total += (i-1)//middle
    if total > M:
        minn = middle + 1
    else:
        maxx = middle - 1
print(minn)
