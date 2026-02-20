N, M = map(int, input().split())
board = [input().strip() for _ in range(N)]

# WB 시작 체스판
WB = []
for i in range(8):
    row = ""
    for j in range(8):
        if (i + j) % 2 == 0:
            row += 'W'
        else:
            row += 'B'
    WB.append(row)

# BW 시작 체스판
BW = []
for i in range(8):
    row = ""
    for j in range(8):
        if (i + j) % 2 == 0:
            row += 'B'
        else:
            row += 'W'
    BW.append(row)

answer = float('inf')

# 모든 8x8 시작점 탐색
for i in range(N - 7):
    for j in range(M - 7):

        wb_cnt = 0
        bw_cnt = 0

        # 8x8 비교
        for x in range(8):
            for y in range(8):
                if board[i+x][j+y] != WB[x][y]:
                    wb_cnt += 1
                if board[i+x][j+y] != BW[x][y]:
                    bw_cnt += 1

        answer = min(answer, wb_cnt, bw_cnt)

print(answer)