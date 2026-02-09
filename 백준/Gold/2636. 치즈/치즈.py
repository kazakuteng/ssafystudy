from collections import deque

# N = int(input())

N, M = map(int, input().split())
cheeze = [list(map(int, input().split())) for _ in range(N)]
total = 0
time = 0
dx = [0, -1, 0 ,1]
dy = [-1, 0, 1, 0]

for i in cheeze:
    total += i.count(1)

while total > 0:
    last = total
    visited = [[False for _ in range(M)] for _ in range(N)]
    que = deque()
    que.append((0,0))
    melt = set()
    visited[0][0] = True
    while que:
        na, nb = que.popleft()
        
        for i in range(4):
            a = na + dx[i]
            b = nb + dy[i]
            if 0<= a <= N-1 and 0 <= b <= M-1:
                if not visited[a][b]:
                    if cheeze[a][b] == 0:
                        visited[a][b] = True
                        que.append((a,b))
                    else:
                        melt.add((a,b))
    for i in melt:
        total -= 1
        cheeze[i[0]][i[1]] = 0
    
    time += 1
print(time)
print(last)


        