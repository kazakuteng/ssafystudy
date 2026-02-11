N, M = map(int, input().split())
a = list(map(int, input().split()))
total = 0
for i in range(M):
    total += a[i]

maxx = total
for i in range(M, N):
    
    total += a[i] - a[i-M]
    
    if total > maxx:
        maxx = total
print(maxx)

    