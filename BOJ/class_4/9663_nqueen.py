# n-queen
def queen(row, k):
    global cnt
    if row == k:
        cnt += 1
        return

    else:
        for j in range(N):
            can_position = True
            # 열 검사
            for l in range(0, row+1):
                if board[l][j] == 1:
                    can_position = False

            # 대각선 1 검사
            for l in range(0, row+1):
                if 0 <= j-l < N and board[row-l][j-l] == 1:
                    can_position = False

            # 대각선 2 검사
            for l in range(0, row+1):
                if 0 <= j+l < N and board[row-l][j+l] == 1:
                    can_position = False

            if can_position == True:
                board[row][j] = 1
                queen(row+1, k)
                board[row][j] = 0


N = int(input())
board = [[0]*N for _ in range(N)]
cnt = 0
queen(0, N)
print(cnt)
