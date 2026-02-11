def bfs(start):
    visited = [-1] * (N+1)
    visited[start] = 0
    que = deque()
    que.append((start, 0))
    while que:
        cur = que.pop()
        for i in road[cur[0]]:
            if visited[i[0]] == -1:
                visited[i[0]] = cur[1] + i[1]
                que.append((i[0], visited[i[0]]))
    return visited

from collections import deque
N = int(input())
road = [[] for _ in range(N+1)]
for i in range(N-1):
    a,b,c = map(int, input().split())
    road[a].append((b,c))
    road[b].append((a,c))

first = bfs(1)
nextt = first.index(max(first))
second = bfs(nextt)
print(max(second))
