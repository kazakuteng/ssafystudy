from heapq import heapify, heappop, heappush

N, E = map(int,input().split())
town = [[] for _ in range(N+1)]
for i in range(E):
    a = list(map(int,input().split()))
    town[a[0]].append((a[1], a[2]))
    town[a[1]].append((a[0], a[2]))

b = list(map(int,input().split()))


def dij(start):
    
    
    H = []
    W = [float("inf") for _ in range(N+1)]
    W[start] = 0
    heappush(H, (0,start))
    while H:
        cost, now = heappop(H)  
        
        if cost > W[now]:
            continue
        for j in town[now]:
            if W[now] +  j[1] < W[j[0]]:
                W[j[0]] = W[now] +  j[1]
                heappush(H, (W[j[0]], j[0]))
    return W

first = dij(1)[b[0]] + dij(b[0])[b[1]] + dij(b[1])[N]
second = dij(1)[b[1]] + dij(b[1])[b[0]] + dij(b[0])[N]
if min(first, second) >= float('inf') :
    print(-1)
else:
    print(min(first, second))