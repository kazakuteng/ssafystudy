from itertools import permutations
N, M = map(int, input().split())
a = list(map(int, input().split()))
b = list(permutations(a,M))
b = list(set(b))
b.sort()

for i in b:
    print(*i)