import sys
from collections import deque

# 왜 empty que에서 빼는 현상이 생기는 건지?
# 높이가 같을 때, 왼쪽에서 먼저 빼기 위해서 어떻게 처리해야 할지?

dx = [-1, -1, 0, 0]
dy = [0, 0, -1, 1]

def babyshark (i, j):
    # i, j는 시작하는 정점
    global que
    global time
    global arr
    global shark_size
    global eat

    visit_cnt = 1
    visited = [[-1]*n for _ in range(n)]
    visited[i][j] = 0 # 처음 방문한 곳의 visit 처리
    eat_list = []
    while que:
        l = len(que)
        for _ in range(l):
            si, sj = que.popleft()
            for d in range(4):
                ni, nj = si + dx[d], sj + dy[d]
                if 0 <= ni < n and 0 <= nj < n and visited[ni][nj] == -1 and arr[ni][nj] <= shark_size:
                    visited[ni][nj] = visit_cnt
                    que.append((ni,nj))
                    if 0 < arr[ni][nj] < shark_size:
                        eat_list.append((ni, nj))
        visit_cnt += 1
        # 다음으로 이동할 곳 탐색 (먹을 생선)
        if eat_list:
            eat += 1
            if eat == shark_size:  # 상어의 크기 처리
                eat = 0
                shark_size += 1

            ei, ej = min(eat_list) # 다음으로 이동할 곳 선정
            que.clear()
            que.append((ei, ej)) # 이동할 곳 큐에 넣기
            arr[ei][ej] = 0 # 먹음처리
            time += arr[ei][ej] # 이동하는데 걸린 시간 추가
            babyshark(ei, ej) # 새로운 곳에서 재실행


n = int(sys.stdin.readline())
arr = []
for _ in range(n):
    arr.append(list(map(int, sys.stdin.readline().split())))

shark_size = 2 # 최초 상어의 크기
eat = 0 # 지금까지 먹은 생선
time = 0 # 최종 걸린시간

que = deque() # bfs를 위한 준비

flag = True
for i in range(n):  # 최초 상어 위치를 탐색한다.
    for j in range(n):
        if arr[i][j] == 9:
            flag = False
            break
    if not flag:
        break

que.append((i, j))
arr[i][j] = 0
babyshark(i, j)
print(time)