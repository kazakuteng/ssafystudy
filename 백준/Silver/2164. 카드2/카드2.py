from collections import deque
N = int(input())
a = [i+1 for i in range(N-1,-1,-1)]
a = deque(a)

while len(a) != 1:
    
    a.pop()
    

    a.rotate(1)
    
    
print(a[0])
