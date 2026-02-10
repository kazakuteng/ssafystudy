import sys
N = int(sys.stdin.readline())
b = 0
for i in range(1, N+1):
    a = i
    temp = i
    while temp > 0:
        a += temp % 10
        temp //= 10
    
    if a == N:
        b = i
        print(b)
        break
if not b:
    print(b)