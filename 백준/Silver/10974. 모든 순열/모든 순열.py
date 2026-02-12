from itertools import permutations
N = int(input())
a = list(permutations([i+1 for i in range(N)], N))
for i in a:
    print(*i)