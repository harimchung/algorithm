import sys

N = int(sys.stdin.readline())
nl = [int(sys.stdin.readline()) for _ in range(N)]
nl.sort()
for n in nl:
    print(n)

