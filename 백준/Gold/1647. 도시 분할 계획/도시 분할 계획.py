N, M =map(int, input().split())
road = []
for i in range(M):
    road.append(list(map(int, input().split())))

road.sort(key = lambda i : i[2])
parent = [i for i in range(N+1)]

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    a = find(a)
    b = find(b)
    if a == b:
        return
    else:
        if a < b:
            parent[b] = a
        else:
            parent[a] = b
    return

cnt = 0
total = 0
for i in road:
    if cnt == N-2:
        break
    if find(i[0]) != find(i[1]):
        union(i[0], i[1])
        cnt +=1
        total += i[2]
print(total)