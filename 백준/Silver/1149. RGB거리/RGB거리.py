N = int(input())
# N, M = map(int, input().split())
a = [list(map(int, input().split())) for i in range(N)]

for i in range(1, N):
    for j in range(3):
        if j == 0:
            a[i][0] += min(a[i-1][1], a[i-1][2])
        if j == 1:
            a[i][1] += min(a[i-1][0], a[i-1][2])
        if j == 2:
            a[i][2] += min(a[i-1][0], a[i-1][1])
print(min(a[-1]))   