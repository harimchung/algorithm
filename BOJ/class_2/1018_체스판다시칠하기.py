def change1(chess):
    example1 = [['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'], ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'], ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'], ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'], ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'], ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'], ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'], ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B']]
    cnt = 0
    for i in range(8):
        for j in range(8):
            if chess[i][j] != example1[i][j]:
                cnt += 1
    return cnt

def change2(chess):
    example2 = [['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'], ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'], ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'], ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'], ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'], ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'], ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'], ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W']]
    cnt = 0
    for i in range(8):
        for j in range(8):
            if chess[i][j] != example2[i][j]:
                cnt += 1
    return cnt

N, M = map(int, input().split())
min_V = 100000
board = [list(input()) for _ in range(N)]

# N x M 에 대해서 8x8로 잘라서 순회하는 방법

for i in range(0, N-8+1):
    for j in range(0, M-8+1):
        chess = [[] for _ in range(8)]
        for k in range(8):
            chess[k] = board[i+k][j:j+8]
        tmp = min(change1(chess), change2(chess))

        if tmp < min_V :
           min_V = tmp

print(min_V)
