
def ver(si, sj):
    global cnt
    if sj == N-1:
        if si != N-1:
            return
        cnt += 1
        return

    else:
        # 만약 가로로 갈 수 있으면 가로로간다
        ni, nj = si, sj+1
        if nj < N and arr[ni][nj] == 0:
            ver(ni, nj)
            # 만약 대각선으로 갈 수 있으면 대각선으로 간다. (세로에 대해서만 검사가 필요하다)
            ni, nj = si+1, sj+1
            if ni < N and arr[ni][nj] == 0 and arr[ni][nj-1] == 0:
                dia(ni, nj)

def hor(si, sj):
    global cnt
    if si == N-1:
        if sj != N-1:
            return
        cnt += 1
        return

    else:
        # 만약 세로로 갈 수 있으면 세로로 간다
        ni, nj = si+1, sj
        if ni < N and arr[ni][nj] == 0:
            hor(ni, nj)
            # 만약 대각선으로 갈 수 있으면 대각선으로 간다
            ni, nj = si+1, sj+1
            if nj < N and arr[ni][nj] == 0 and arr[ni-1][nj] == 0:
                dia(ni, nj)

def dia(si, sj):
    global cnt
    if si == sj == N-1:
        cnt += 1
        return
    else:
        # 만약 가로로 갈 수 있으면 가로로 간다
        ni, nj = si, sj+1
        if nj < N and arr[ni][nj] == 0:
            ver(ni, nj)
        # 만약 세로로 갈 수 있으면 세로로 간다
        ni, nj = si+1, sj
        if ni < N and arr[ni][nj] == 0:
            hor(ni, nj)
            # 만약 대각선으로 갈 수 있으면 대각선으로 간다
            ni, nj = si+1, sj + 1
            if nj < N and arr[ni][nj] == 0 and arr[ni-1][nj] == 0:
                dia(ni, nj)


N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
visited = [[0]*N for __ in range(N)]
cnt = 0
if not visited[N-1][N-1] == 1:
    ver(0, 1) # 처음 시작점은 (0,1) 이며 최초 상태는 가로로 놓여있다.

print(cnt)

