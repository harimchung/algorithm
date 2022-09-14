import sys
import heapq
heap = []
n = int(sys.stdin.readline())
for _ in range(n):
    i = int(sys.stdin.readline())
    if i == 0:
        if heap:
            s = heapq.heappop(heap)
            print(s)
        else:
            print(0)
    else:
        heapq.heappush(heap, i)