N = int(input())
for i in range(N):
    a, b = input().split()
    a = int(a)
    c = ''
    for i in b:
        for _ in range(a):
            c += i
    print(c)