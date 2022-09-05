import sys
from collections import deque

t = int(sys.stdin.readline())
for _ in range(t):
    order = sys.stdin.readline()
    n = int(sys.stdin.readline())
    num_list = deque()
    num_str = sys.stdin.readline().split(',')
    for j in num_str:
        if j.isdecimal():
            num_list.append(j)
    print(num_list)
    # ans = 0
    # for i in order:
    #     if i == "R":
    #         num_list = num_list[::-1]
    #     elif i == "D":
    #         if num_list:
    #             num_list.pop(0)
    #         else:
    #             print("error")
    #             break

