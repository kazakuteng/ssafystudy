import sys
sys.setrecursionlimit(10**6)

def root(start, length):
    visited[start] = True
    
    
    if start == R and len(road[start]) != 1:
        
        return (start, length)
    if start != R and len(road[start]) != 2:
        return (start, length)
    for i in road[start]:
        if not visited[i[0]]:
            
            return root(i[0], i[1] + length)
            

def leaf(start, length):
    global maxx
    visited[start] = True
    if len(road[start]) == 1:
        if length > maxx:
            maxx = length
    for i in road[start]:
        if not visited[i[0]]:
            
            leaf(i[0], i[1] + length)
            visited[i[0]] = False
    

N, R = map(int, input().split()) 
road = [[] for _ in range(N+1)]

for i in range(N-1):
    a,b,c = map(int, input().split())
    road[a].append((b,c))    
    road[b].append((a,c))   

visited = [False] * (N+1)
maxx = 0
nextt = root(R, 0)

leaf(nextt[0], 0)
print(nextt[1], maxx)