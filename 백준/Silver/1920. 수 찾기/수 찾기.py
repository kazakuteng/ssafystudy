N = int(input())
a = list(map(int, input().split()))
M = int(input())
b = list(map(int, input().split()))
c = {}
for i in a:
    c[i] = 1
for i in b:
    if i in c:
        print(1)
    else:
        print(0)