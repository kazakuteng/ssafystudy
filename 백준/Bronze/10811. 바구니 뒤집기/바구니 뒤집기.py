N, M = map(int, input().split())
nlist = [i+1 for i in range(N)]
for i in range(M):
    a, b = map(int, input().split())
    for j in range(a-1,b):
        if j < b-1-j+a-1:
            nlist[j], nlist[b-1-j+a-1] =  nlist[b-1-j+a-1], nlist[j]
for i in nlist:
    print(i, end = " ")