from heapq import heapify, heappop, heappush

N = int(input())
time = [0] * (N+1)


visited = [False] * (N+1)

length = [0] * (N+1)
cur = []

road = [[] for _ in range(N+1)]
for i in range(N):
    a= list(map(int, input().split()))
    time[i+1] = a[0]
    for j in range(1, len(a)-1):

        road[a[j]].append(i+1)
    
        length[i+1] += 1



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
                
                
time = time[1:]
print(*time)


