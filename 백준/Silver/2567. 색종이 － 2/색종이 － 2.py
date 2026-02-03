from collections import defaultdict
T = int(input())
black = defaultdict(int)
for _ in range(T):
    N, M = map(int, input().split())
    for i in range(N, N+10):
        for j in range(M, M+10):
            
            
            black[(i, j)] += 1
total = 0
for (a, b) in black:
    
    cnt = 0
    if (a-1, b) in black:
        cnt+=1
    if (a+1, b) in black:
        cnt+=1
    if (a, b-1) in black:
        cnt+=1
    if (a, b+1) in black:
        cnt+=1
    if cnt == 3:
        total += 1
    if cnt == 2:
        total += 2
print(total)