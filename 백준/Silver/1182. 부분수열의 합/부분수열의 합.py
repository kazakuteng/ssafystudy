N, S = map(int, input().split())

number = list(map(int, input().split()))
cnt = 0
def dfs(depth,  total, index):
    global cnt
    if  index == 1 and total == S:
        cnt += 1
    
            
    if depth == N:
        
            
        return
    
    else:
        dfs(depth+1,  total+number[depth], 1)
        dfs(depth+1,  total, 0)
dfs(0,0,0)
print(cnt)