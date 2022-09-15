import sys
from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

n = int(sys.stdin.readline())
arr = []
for _ in range(n):
    arr.append(list(map(int, sys.stdin.readline().split())))

shark_size = 2 # 최초 상어의 크기
visit_cnt = 0 # 얼마만에 칸에 도달했는지 구하기 위한 변수
eat = 0 # 지금까지 먹은 생선
time = 0 # 최종 걸린시간

que = deque() # bfs를 위한 준비
visited = [[-1]*n for _ in range(n)]

for i in range(n):  # 최초 상어 위치를 탐색한다.
    for j in range(n):
        if arr[i][j] == 9:
            que.append((i,j))
            visited[i][j] = visit_cnt
            arr[i][j] = 0
            break


while que:  # visited 배열을 통해서 bfs를 진행한다. (상, 하, 좌, 우 순서로 탐색)
    l = len(que)
    visit_cnt += 1
    for _ in range(l):
        si, sj = que.popleft()
        for d in range(4):
            ni, nj = si+dx[d], sj+dy[d]
            if 0 <= ni < n and 0 <= nj < n and visited[ni][nj] == -1 and arr[ni][nj] <= shark_size:
                visited[ni][nj] = visit_cnt
                que.append((ni, nj))
                if 0 < arr[ni][nj] < shark_size: # 먹을 수 있는 물고기 발견
                    eat += 1
                    arr[ni][nj] = 0 # 잘 먹었습니다.
                    if eat == shark_size:
                        eat = 0
                        shark_size += 1
                    time += visited[ni][nj]
                    que.clear()
                    # visited 배열 갱신
                    visited = [[-1] * n for _ in range(n)]
                    visit_cnt = 0
                    visited[ni][nj] = visit_cnt
                    que.append((ni,nj))
                    break


print(time)

