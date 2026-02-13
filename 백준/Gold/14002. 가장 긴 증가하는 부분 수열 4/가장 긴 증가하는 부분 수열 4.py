N = int(input())
A = list(map(int, input().split()))

lis = [[1,[A[_]]] for _ in range(N)]

for i in range(1, N):
    for j in range(i):
        if A[i] > A[j]:
            if lis[j][0]+1 > lis[i][0]:
                lis[i][0] = lis[j][0]+1
                lis[i][1] = lis[j][1][:] + [A[i]]

lis.sort()
print(lis[-1][0])
print(*lis[-1][1])

