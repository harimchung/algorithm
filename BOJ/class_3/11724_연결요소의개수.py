import sys


n, m = map(int, sys.stdin.readline().split())
# m줄에 걸쳐서 간선이 주어진다.
# 간선의 정보를 담은 인접리스트 adj를 만든다.
adj = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    adj[a].append(b)
    adj[b].append(a)


visited = [0] * (n+1)
visited[0] = 1
cnt = 0
stack = []
s = 1
# 1부터 dfs(깊이 우선탐색) 을 통해서 갈 수 있는 곳 까지 간다.
while sum(visited) < n+1:
    visited[s] = 1
    while True:
        for i in adj[s]:
            if visited[i] == 0:
                stack.append(s)
                s = i
                visited[s] = 1
                break
        else:
            if stack:
                s = stack.pop()
            else:
                cnt += 1
                # 다음 s 값 탐색
                for i in range(1, n + 1):
                    if visited[i] == 0:
                        s = i
                        break
                break



print(cnt)