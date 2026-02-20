T = int(input())
arr = [0]* 13
arr[1] = 1
arr[2] = 2
arr[3] = 4
for i in range(4, 13):
    arr[i] = arr[i-1]+arr[i-2]+arr[i-3]
for i in range(T):
    N = int(input())
    print(arr[N])