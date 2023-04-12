N, M = map(int, input().split())
fuels = [list(map(int, input().split())) for _ in range(N)]

# 완전 탐색으로 방향을 바꿔본다.
dx = [1, 1, 1]
dy = [-1, 0, 1]
ans = 10000000

def calculate_fuel(i, j, direction, price):
    global ans
    if i == N-1:
        ans = min(ans, price)
        return

    if price >= ans:
        return

    for d in range(3):
        if d == direction:
            continue
        else:
            ni, nj = i + dx[d], j + dy[d]
            if 0 <= ni < N and 0 <= nj < M:
                fuel = fuels[ni][nj]
                calculate_fuel(ni, nj,d, price + fuel)

                
for x in range(M):
    for y in range(3): 
        calculate_fuel(0, x, y, fuels[0][x])

print(ans)