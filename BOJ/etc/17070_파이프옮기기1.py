import sys
sys.setrecursionlimit(10**6)

def ver(si, sj):
    global cnt
    if si == sj == N-1:
        cnt += 1
        return
    else:
        # 만약 가로로 갈 수 있으면 가로로간다
        ni, nj = si, sj+1
        if nj < N and arr[ni][nj] == 0:
            ver(ni, nj)
            # 만약 대각선으로 갈 수 있으면 대각선으로 간다
            ni, nj = si+1, sj+1
            if ni < N and arr[ni][nj] == 0 and arr[ni-1][nj]== 0:
                dia(ni, nj)

def hor(si, sj):
    global cnt
    if si ==  sj == N-1:
        cnt += 1
        return
    else:
        # 만약 세로로 갈 수 있으면 세로로 간다
        ni, nj = si+1, sj
        if ni <N  and arr[ni][nj] == 0:
            hor(ni, nj)
            # 만약 대각선으로 갈 수 있으면 대각선으로 간다
            ni, nj = si+1, sj+1
            if  nj < N and arr[ni][nj] == 0 and arr[ni-1][nj]== 0:
                dia(ni, nj)

def dia(si, sj):
    global cnt
    if si == sj == N-1:
        cnt += 1
        return
    else:
        # 만약 가로로 갈 수 있으면 가로로 간다
        ni, nj = si, sj+1
        if nj <N and arr[ni][nj] == 0:
            ver(ni, nj)
        # 만약 세로로 갈 수 있으면 세로로 간다
        ni, nj = si+1, sj
        if ni < N and arr[ni][nj] == 0:
            hor(ni, nj)
            # 만약 대각선으로 갈 수 있으면 대각선으로 간다
            ni, nj = si+1, sj + 1
            if nj < N and arr[ni][nj] == 0 and arr[ni-1][nj] == 0:
                dia(ni, nj)


N = int(sys.stdin.readline())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
cnt = 0
ver(0, 1) # 처음 시작점은 (0,1) 이며 최초 상태는 가로로 놓여있다.
print(cnt)

