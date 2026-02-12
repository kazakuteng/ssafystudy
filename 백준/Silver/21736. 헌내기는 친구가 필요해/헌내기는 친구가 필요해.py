from collections import deque

N, M = map(int, input().split())
arr = [input() for _ in range(N)]
di = [-1,0,1,0]
dj = [0,-1,0,1]
start = 0
visited = [[False] * M for _ in range(N)]
for i in range(N):
    for j in range(M):
        if arr[i][j] == 'I':
            start = (i, j)
        if arr[i][j] == 'X':
            visited[i][j] = True

que = deque()
que.append(start)
total = 0

while que:
    x, y = que.popleft()
    
    for i in range(4):
        dx = x + di[i]
        dy = y + dj[i]
        if 0<=dx<N and 0<=dy<M:
            if not visited[dx][dy]:
                visited[dx][dy] = True
                if arr[dx][dy] == 'P':
                    total += 1
                que.append((dx,dy))

if total:
    print(total)
else:
    print('TT')
