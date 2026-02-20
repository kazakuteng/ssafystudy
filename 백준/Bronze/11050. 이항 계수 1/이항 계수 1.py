from itertools import combinations
N, M = map(int, input().split())
a = [0] * N
print(len(list(combinations(a, M))))