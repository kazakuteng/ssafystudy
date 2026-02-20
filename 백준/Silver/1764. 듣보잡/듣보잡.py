N, M = map(int, input().split())
a = []
b = []
for i in range(N):
    a.append(input())
for i in range(M):
    b.append(input())
a = set(a)
b = set(b)
c = a & b
print(len(c))
c = list(c)
c.sort()
for i in c:
    print(i)