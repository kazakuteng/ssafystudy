from collections import deque

def bfs(start):
    que.append(start)
    visited[start[0]][start[1]] = True
    vocnt = 1
    
    while que:
        x, y = que.popleft()
        for i in range(4):
            dx = x + di[i]
            dy = y + dj[i]
            if 0<= dx < N and 0<= dy < M:
                if not visited[dx][dy]:
                    visited[dx][dy] = True
                    vocnt += 1
                    que.append((dx, dy))
    total[0] += 1
    if maxx[0] < vocnt:
        maxx[0] = vocnt
    return

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
visited = [[False]*M for _ in range(N)]
for i in range(N):
    for j in range(M):
        if arr[i][j] == 0:
            visited[i][j] = True
que = deque()
total = [0]
maxx = [0]
di = [-1,0,1,0]
dj = [0,-1,0,1]
for i in range(N):
    for j in range(M):
        if not visited[i][j]:
            bfs((i, j))
print(total[0])
print(maxx[0])