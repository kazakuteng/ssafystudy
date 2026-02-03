

N = int(input())
people = []
for i in range(N):
    a, b = map(int, input().split())
    people.append((a,b))
people_huge = []
for a, b in people:
    huge = 1
    for c, d in people:
        if a < c and b < d:
            huge += 1
    people_huge.append(huge)
for i in people_huge:
    print(i, end = " ")