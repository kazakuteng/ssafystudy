from itertools import combinations, permutations

N = int(input())
team = [list(map(int, input().split())) for _ in range(N)]


member = list(combinations([i for i in range(N)], N//2))

l = len(member)
total = []
for i in range(l//2):
    first = 0
    second = 0
    for x, y in permutations(member[i], 2):
        first += team[x][y]
    for x, y in permutations(member[l-1-i], 2):
        second += team[x][y]
    total.append(max(first - second, second - first))
print(min(total))