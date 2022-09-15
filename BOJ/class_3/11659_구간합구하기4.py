import sys

n, m = map(int, sys.stdin.readline().split())
number = list(map(int, sys.stdin.readline().split()))
for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    print(sum(number[a-1:b]))