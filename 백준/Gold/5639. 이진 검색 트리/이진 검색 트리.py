
import sys
# sys.stdin = open("input.txt", "r")

sys.setrecursionlimit(10**6)
arr= []
while True:
    try:
        arr.append(int(sys.stdin.readline())) 
    except:
        break

def dfs(start, endd):
    if start > endd:
        return
    root = arr  [start]
    middle = endd + 1
    for i in range(start+1, endd+1):
        if arr[i] > root:
            middle = i
            break
    dfs(start + 1 , middle - 1)
    dfs(middle, endd)
    print(root)
    
dfs(0, len(arr)-1)