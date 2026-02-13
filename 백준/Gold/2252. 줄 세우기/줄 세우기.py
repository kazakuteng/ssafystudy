from collections import deque

N, M = map(int, input().split())

que = deque()
visited = [False] * (N+1)

length = [0] * (N+1)
answer = []
road = [[] for _ in range(N+1)]
for i in range(M):
    a, b = map(int, input().split())
    road[a].append(b)
    length[b] += 1

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

print(*answer)
