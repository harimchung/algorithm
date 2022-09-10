import sys


# 컴퓨터의 수는 n으로 주어진다.
n = int(sys.stdin.readline().rstrip())

# 연결되어있는 컴퓨터 쌍의 수가 주어진다.
# 정보를 받을 인접리스트를 adj에 저장한다.
m = int(sys.stdin.readline().rstrip())
adj = [[] for _ in range (n+1)]
for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    adj[a].append(b)
    adj[b].append(a)

# 입력을 다 받고 난 후, 1번 컴퓨터가 웜 바이러스에 걸렸을 떄,
# 웜 바이러스에 걸리게 되는 컴퓨터의 수를 출력한다.
# dfs
visited = [0]*(n+1)
stack = []

s = 1
visited[s] = 1
cnt = 0
while True:
    for i in adj[s]:
        if visited[i] == 0:
            stack.append(s)
            s = i
            visited[s] = 1
            cnt += 1
            break
    else:
        if stack:
            s = stack.pop()
        else:
            break
print(cnt)