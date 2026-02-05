N, K = map(int,input().split())
line = []
for i in range(N):
    a = int(input())
    line.append(a)
line.sort()
start = 1
end = max(line)

while start <= end:
    middle = (start + end) // 2
    total = 0

    
    for i in line:
        total += i // middle
    if total >= K:

        start = middle + 1
    else:
        end = middle -1

print(end)
