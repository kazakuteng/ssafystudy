cnt0 = 0
cnt1 = 0
N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
def cut(x, y, big):
    check = True
    global cnt0, cnt1
    for i in range(x, x+big):
        if check == False:
            break
        for j in range(y, y+big):
            if arr[x][y] != arr[i][j]:
                check = False
                break
    if check == True:
        if arr[x][y] == 0:
            
            cnt0 += 1
        else:
            
            cnt1 += 1
    else:
        cut(x,y,big//2)
        cut(x+big//2,y, big//2)
        cut(x,y+big//2, big//2)
        cut(x+big//2,y+big//2, big//2)
cut(0,0,N)
print(cnt0)
print(cnt1)