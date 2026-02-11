N = int(input())
sol = list(map(int, input().split()))
pluss = []
minuss = []
for i in sol:
    if i > 0:
        pluss.append(i)
    else:
        minuss.append(i)

pluss.sort()
minuss.sort(reverse=True)
pluscnt = 0
minuscnt = 0
plusminus = (0, 0, float("inf"))
a = len(pluss)
b = len(minuss)
pp = float("inf")
mm = float("inf")
if a == 0:
    print(minuss[1], minuss[0])
elif b == 0:
    print(pluss[0], pluss[1])
else:
    if a >1:
        pp = pluss[0] + pluss[1]
    if b > 1:
        mm = - minuss[0] - minuss[1]
    while True:
        c = pluss[pluscnt] + minuss[minuscnt]
        if abs(c) < plusminus[2]:
            plusminus = (pluscnt, minuscnt, abs(c))
        if c > 0:
            minuscnt += 1
            if minuscnt == b:
                break
        if c < 0:
            pluscnt += 1
            if pluscnt == a:
                break
        if c == 0:
            break
    if min(plusminus[2], mm, pp) == mm:
        print(minuss[1], minuss[0])
    elif min(plusminus[2], mm, pp) == pp:
        print(pluss[0], pluss[1])
    else:
        print(minuss[plusminus[1]], pluss[plusminus[0]])
