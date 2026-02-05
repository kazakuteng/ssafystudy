from heapq import heapify, heappop, heappush

N = int(input())
H = []

# N, K = map(int,input().split())
for i in range(N):
    a = int(input())
    if a != 0:
        heappush(H, (abs(a), a))
    else:
        if len(H) == 0:
            print(0)
        else:
            b = heappop(H)
            print(b[1])