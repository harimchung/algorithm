import sys
from collections import deque
# 첫 줄에 수빈이가 있는 위치 n과 동생이 있는 위치k 가 주어진다.
n, k = map(int, sys.stdin.readline().split())
visited = [0]*100001
que = deque()
que.append(n)
cnt = 1
visited[n] = cnt


# 수빈이가 한 번 돌때마다 cnt에 1씩 추가시킨다.
while True:
    if visited[k] != 0:
        break
    cnt += 1
    for _ in range(len(que)):
        s = que.popleft()
        if 0<=s-1<100001 and visited[s-1] == 0:
            visited[s-1] = cnt
            que.append(s-1)
        if 0<=s+1<100001 and visited[s + 1] == 0:
            visited[s+1] = cnt
            que.append(s + 1)
        if 0<=2*s<100001 and visited[2*s] == 0:
            visited[2*s] = cnt
            que.append(2*s)

print(visited[k]-1)