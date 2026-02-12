from collections import deque

def bfs(start):
    que.append(start)
    visited[start[0]][start[1]] = True
    vocnt = [0,0]
    if arr[start[0]][start[1]] == 'v':
        vocnt[0] += 1
    if arr[start[0]][start[1]] == 'o':
        vocnt[1] += 1
    
    while que:
        x, y = que.popleft()
        for i in range(4):
            dx = x + di[i]
            dy = y + dj[i]
            if 0<= dx < N and 0<= dy < M:
                if not visited[dx][dy]:
                    visited[dx][dy] = True
                    if arr[dx][dy] == 'v':
                        vocnt[0] += 1
                    if arr[dx][dy] == 'o':
                        vocnt[1] += 1
                    que.append((dx, dy))
    if vocnt[0] < vocnt[1]:
        vo[1] += vocnt[1]
    else:
        vo[0] += vocnt[0]

N, M = map(int, input().split())
arr = [input() for _ in range(N)]
visited = [[False]*M for _ in range(N)]
for i in range(N):
    for j in range(M):
        if arr[i][j] == '#':
            visited[i][j] = True
que = deque()
vo = [0, 0]
di = [-1,0,1,0]
dj = [0,-1,0,1]
for i in range(N):
    for j in range(M):
        if not visited[i][j]:
            bfs((i, j))
print(vo[1], vo[0])