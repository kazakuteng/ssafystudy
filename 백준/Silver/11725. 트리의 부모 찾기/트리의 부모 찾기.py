from collections import deque


N = int(input())
a = [0 for _ in range(N+1)]
a[1] = 1
road = [[] for _ in range(N+1)]
for _ in range(N-1):
    x, y = map(int, input().split())
    road[x].append(y)
    road[y].append(x)
que = deque()
que.append(1)
while que:
    t = que.popleft()
    for i in road[t]:
        if not a[i]:
            a[i] = t
            que.append(i)
for i in range(2, N+1):
    print(a[i])
