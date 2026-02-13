from collections import deque

N, M = map(int, input().split())

que = deque()
visited = [False] * (N+1)

length = [0] * (N+1)
answer = []
road = [[] for _ in range(N+1)]
for i in range(M):
    a = list(map(int, input().split()))
    for j in range(1,len(a)-1):
        road[a[j]].append(a[j+1])
    
        length[a[j+1]] += 1

for i in range(1, N+1):
    if length[i] == 0:
        que.append(i)
        visited[i] = True


while que:
    a = que.popleft()
    answer.append(a)
    for i in road[a]:
        
        if not visited[i]:
            
            length[i] -= 1
            if length[i] == 0:
                visited[i] = True
                que.append(i)
if len(answer) < N:
    print(0)
else:
    for i in answer:
        print(i)
