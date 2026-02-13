from heapq import heapify, heappop, heappush
T = int(input())
for c in range(T):
    N, M = map(int, input().split())
    time = [0] + list(map(int, input().split()))
    
    
    visited = [False] * (N+1)

    length = [0] * (N+1)
    cur = []
    
    road = [[] for _ in range(N+1)]
    for i in range(M):
        a, b = map(int, input().split())
        road[a].append(b)
        length[b] += 1

    W = int(input())

    for i in range(1, N+1):
        if length[i] == 0:
            heappush(cur, (time[i], i))
            visited[i] = True



    while cur:
        t, a = heappop(cur)
        
        for i in road[a]:
            if not visited[i]:
                
                length[i] -= 1
                if length[i] == 0:
                    visited[i] = True
                    time[i] += t
                    heappush(cur, (time[i], i))
                    
                    
    answer = time[W]
    print(answer)
