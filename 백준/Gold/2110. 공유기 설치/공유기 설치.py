N, C = map(int, input().split())
arr = [int(input()) for _ in range(N)]

arr.sort()
left = 1
right = arr[-1] - arr[0]
while left <= right:
    middle = (left + right) //2 
    total = 1
    index = 0
    for i in range(1, N):
        if arr[i] - arr[index] >= middle:
            total += 1
            index = i
    
    if total < C:
        right = middle - 1
    
    else:
        left = middle + 1    
print(right)

