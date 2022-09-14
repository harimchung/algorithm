import sys
import heapq

n = int(sys.stdin.readline())
heap = []
for _ in range(n):
    i = int(sys.stdin.readline())
    if i == 0:
        if heap:
            max_item = heapq.heappop(heap)[1]
            print(max_item)
        else:
            print(0)
    else:
        heapq.heappush(heap, (-i, i))