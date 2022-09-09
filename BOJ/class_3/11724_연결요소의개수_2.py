import sys
sys.setrecursionlimit(10**7)

def dfs(s):
    visited[s] = 1
    for i in adj[s]:
        if visited[i] == 0:
            dfs(i)

n, m = map(int, sys.stdin.readline().split())
# m줄에 걸쳐서 간선이 주어진다.
# 간선의 정보를 담은 인접리스트 adj를 만든다.
adj = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    adj[a].append(b)
    adj[b].append(a)


visited = [0] * (n+1)
cnt = 0

# 1부터 dfs(깊이 우선탐색) 을 통해서 갈 수 있는 곳 까지 간다.
for i in range(1, n+1):
    if visited[i] == 0:
        dfs(i)
        cnt += 1

print(cnt)