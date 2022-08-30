import sys
from collections import deque

def tomato(q, g):
    cnt = -1
    while q:
        l = len(q)
        for _ in range(l):
            i, j = q.popleft()
            for di,dj in [[-1,0], [1,0], [0,-1],[0,1]]:
                ni, nj = i+di, j+dj
                if 0<= ni < n and 0<= nj < m and g[ni][nj] == 0:
                    q.append((ni, nj))
                    g[ni][nj] = 1
        cnt += 1

    return cnt


m, n = map(int, sys.stdin.readline().split())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range (n)]

q = deque()
for i in range(n):
    for j in range(m):
        if arr[i][j] == 1:
            q.append((i,j))

ans = tomato(q, arr)
flag = False

for i in range(n):
    for j in range(m):
        if arr[i][j] == 0:
            ans = -1
            flag = True
            break
    if flag:
        break
print(ans)
