from itertools import permutations


N = int(input())
number = []
for c in range(N):
    numm, st, ball = list(input().split())
    st = int(st)
    ball = int(ball)

    if c == 0:
        
        for i in permutations(['1','2','3','4','5','6','7','8','9'], 3):
            numst = 0
            numball = 0
            for j in range(3):
                if numm[j] in i:
                    numball += 1
                if numm[j] == i[j]:
                    numball -= 1
                    numst += 1
            if numball == ball and numst == st:
                number.append(i)
    else:
        number = list(set(number))
        newnumber = []
        for i in number:
            numst = 0
            numball = 0
            for j in range(3):
                if numm[j] in i:
                    numball += 1
                if numm[j] == i[j]:
                    numball -= 1
                    numst += 1
            if numball == ball and numst == st:
                newnumber.append(i)
        number = newnumber[:]
number = list(set(number))
print(len(number))