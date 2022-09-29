def select(i, k, tmp):
    global max_V
    if i == k:
        if tmp > max_V and tmp <= m:
            max_V = tmp
    else:
        for j in range(n):
            if not visited[j]:
                visited[j] = 1
                select(i+1, k, tmp + nl[j])
                visited[j] = 0


n, m = map(int, input().split())
nl = list(map(int, input().split()))
visited = [0]*n
# n개의 카드 중에서 3개를 고를 수 있고, m을 넘지 않으면서 크거나 같아야 한다.
max_V = 0
select(0, 3, 0)
print(max_V)