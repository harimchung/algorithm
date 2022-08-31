import sys
from collections import deque

n, m, v = map(int, sys.stdin.readline().split())

# 정점의 개수만큼 인접행렬을 만든다.
# 정점 번호는 1부터 n번까지이므로, 인덱스의 편의를 위해서 n+1 개를 만든다.
arr = [[0]*(n+1) for _ in range(n+1)]

# m줄에 걸쳐서 간선정보가 주어지면, 인접행렬에 받는다.
# 양방향이므로 두번 넣는다.
for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    arr[a][b] = 1
    arr[b][a] = 1

# dfs
stack = []
visited = [0]*(n+1)

now_i = v
visited[now_i] = 1
print(now_i, end=" ")

while True:
    for i in range(1, n+1):
        if arr[now_i][i] == 1 and visited[i] == 0:
            stack.append(now_i)
            visited[i] = 1
            now_i = i
            print(now_i, end=" ")
            break
    else:
        if stack:
            now_i = stack.pop()
        else:
            break

print()
# bfs
queue = deque()
visited_2 = [0]*(n+1)

visited_2[v] = 1
queue.append(v)
while queue:
    now_j = queue.popleft()
    print(now_j, end=" ")
    for j in range(1, n+1):
        if arr[now_j][j] == 1 and visited_2[j] == 0:
            queue.append(j)
            visited_2[j] = 1