import sys
def tomato(si, sj, g):
    visited = [[0]*m for _ in range(n)]
    global day
    global q
    q = []
    q.append((si, sj))
    visited[si][sj] = 1
    while q:
        i, j = q.pop(0)
        for di,dj in [[-1,0], [1,0], [0,-1],[0,1]]:
            ni, nj = i+di, j+dj


    pass

m, n = map(int, sys.stdin.readline().split())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range (n)]
total = 0
for i in range(n):
    for j in range(m):
        if arr[i][j] == 1:
            tomato(i, j, arr)
