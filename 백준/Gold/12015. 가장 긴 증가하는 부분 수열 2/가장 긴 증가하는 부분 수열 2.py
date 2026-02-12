from bisect import bisect_left

N = int(input())
A = list(map(int, input().split()))

lis = []

for x in A:
    pos = bisect_left(lis, x)
    
    if pos == len(lis):
        lis.append(x)
    else:
        lis[pos] = x

print(len(lis))
