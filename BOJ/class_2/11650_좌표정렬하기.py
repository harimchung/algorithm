import sys

n = int(sys.stdin.readline())
num = []
for _ in range(n):
    a, b = map(int, sys.stdin.readline().split())
    num.append([a,b])
num.sort()

for i in range(n):
    for j in range(2):
        print(num[i][j], end=" ")
    print()