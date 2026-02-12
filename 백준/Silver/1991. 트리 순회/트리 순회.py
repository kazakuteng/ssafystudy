def front(start):
    
    arr1.append(arr[start][0])
    if arr[start][1] != '.':
        
        front(ord(arr[start][1]) - ord('A'))
    if arr[start][2] != '.':
        front(ord(arr[start][2]) - ord('A'))
    return
def middle(start):
    
    
    if arr[start][1] != '.':
        middle(ord(arr[start][1]) - ord('A'))

    arr2.append(arr[start][0])
    if arr[start][2] != '.':
        middle(ord(arr[start][2]) - ord('A'))
    return
def back(start):
    
    
    if arr[start][1] != '.':
        back(ord(arr[start][1]) - ord('A'))
    if arr[start][2] != '.':
        back(ord(arr[start][2]) - ord('A'))
    arr3.append(arr[start][0])
    return

N = int(input())
arr = [list(input().split()) for _ in range(N)]

arr.sort()

arr1 = []
arr2 = []
arr3 = []
front(0)
middle(0)
back(0)
answer1 = ''.join(arr1)
answer2 = ''.join(arr2)
answer3 = ''.join(arr3)
print(answer1)
print(answer2)
print(answer3)
