import sys
from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

n = int(sys.stdin.readline())
arr = [list(map(int, sys.stdin.readline().rstrip())) for _ in range(n)]

# visited 배열 만들기
visited = [[0]*n for _ in range(n)]
que = deque()
danji_list = []

# bfs 적용하기
for i in range(n):
    for j in range(n):
        danji_count = 0
        if arr[i][j] == 1 and visited[i][j] == 0:
            # bfs 적용하기
            danji_count += 1
            visited[i][j] = 1
            que.append((i,j))
            while que:
                si, sj = que.popleft()
                for d in range(4):
                    ni = si + dx[d]
                    nj = sj + dy[d]
                    if 0 <= ni <n and 0 <= nj <n and arr[ni][nj] == 1 and visited[ni][nj]==0:
                        que.append((ni,nj))
                        visited[ni][nj] = 1
                        danji_count += 1
            danji_list.append(danji_count)

danji = len(danji_list)
print(danji)

danji_list.sort()
for danjis in danji_list:
    print(danjis)