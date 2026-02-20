N = int(input())
a = list(map(int, input().split()))
a.sort()
summ = 0
total = 0
for i in a:
    summ+=i
    total += summ
print(total)