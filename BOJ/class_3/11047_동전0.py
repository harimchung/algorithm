import sys

# n종류의 동전을 가지고 k원을 만든다.
n, k = map(int, sys.stdin.readline().split())
coins = []

for _ in range(n):
    coin = int(sys.stdin.readline())
    coins.append(coin)

cnt = 0
while k != 0:
    for i in range(n-1, -1, -1):
        if k // coins[i] > 0:
            cnt += k //coins[i]
            k = k - (k//coins[i])*coins[i]

print(cnt)