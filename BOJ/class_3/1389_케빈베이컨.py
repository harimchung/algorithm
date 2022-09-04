# 케빈 베이컨 수 구하기

import sys
from collections import deque

# 너비탐색을 통해서 각 숫자에 몇 번만에 접근 가능한지 cnt를 반환한다.
def bfs(s, e, g):
    # 시작점(s)과 종료지점(e) 인접행렬(g)이 주어진다.
    visited = [0]*(n+1)
    que = deque()
    visited[s] = 1
    que.append(s)
    cnt = 0
    while que:
        l = len(que)
        for _ in range(l):
            s = que.popleft()
            if s == e:
                return cnt

            for i in range(n+1):
                if g[s][i] == 1 and visited[i] == 0:
                    que.append(i)
                    visited[i] = 1
        cnt += 1

# 시작되는수가 num일 때 모든 친구에 도달하는 베이컨 수의 합 구하기
def kevin(num):
    bacon = 0
    for i in range(1, n+1):
        bacon += bfs(num, i, adj)
    kevin_list[num] = bacon

# 숫자가 들어오면 인접행렬리스트를 만든다.
#  케빈베이컨 수 리스트중에서 최소값비교하는 식을 돌린다.
n, m = map(int, sys.stdin.readline().split())
# 입력을 받을 인접행렬을 만든다.
adj = [[0]*(n+1) for _ in range(n+1)]

# m줄동안 친구관계를 입력받는다. (서로 친구이므로, 왕복가능한 길)
for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    adj[a][b] = 1
    adj[b][a] = 1


# 각 숫자에 대해서 케빈 베이컨 수를 구한다.
kevin_list = [0]*(n+1)
for j in range(1, n+1):
    kevin(j)

minimum_number = 1
for k in range(1, n+1):
    if kevin_list[minimum_number] > kevin_list[k]:
        minimum_number = k
print(minimum_number)
