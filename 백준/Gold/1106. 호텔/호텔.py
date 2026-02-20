N, C = map(int, input().split())
a = [list(map(int, input().split())) for i in range(C)]
b = [float("inf")] * (N+1)
b[0] = 0
for i in range(1, N+1):
    for j in a:
        if j[1]-i<=0:
            b[i] = min(b[i] , b[i - j[1]] + j[0])
            
        else:
            b[i] = min(b[i], j[0])
            

print(b[-1])