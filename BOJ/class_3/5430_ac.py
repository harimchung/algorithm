import sys
from collections import deque

t = int(sys.stdin.readline())
for _ in range(t):
    order = sys.stdin.readline()
    n = int(sys.stdin.readline())

    num_str = sys.stdin.readline().rstrip()
    print(len(num_str))
    # ans = num_str
    # for i in order:
    #
    #     if i == "R":
    #         num_str = num_str[::-1]
    #
    #     elif i == "D":
    #         if num_str:
    #             num_list.pop(0)
    #         else:
    #             ans = "error"
    #             break
    #
    # if not ans == "error":
    #     ans = num_str
    # print(ans)
