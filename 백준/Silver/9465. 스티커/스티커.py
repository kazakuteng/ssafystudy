T = int(input())
# N, M, C = map(int, input().split())
# a = [list(map(int, input().split())) for i in range(N)]

for tc in range(T):
    N = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    for i in range(1, N):
        if i == 1:
            a[i] += b[i-1]
            b[i] += a[i-1]
        else:
            a[i] += max(b[i-1], b[i-2])
            b[i] += max(a[i-1], a[i-2])
    print(max(a[-1], b[-1]))