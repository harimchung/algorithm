# a = 3**100 - 3*(2**100-2) -3
# b = 3 ** 97
# print(a)
# print(b)

# a = [(1,3), (1,2), (2,4)]
# a.pop()
# print(a)

# number = 2
# if not number <= 3 and not number >= 5:
#     print("yes")
# else:
#     print("no")

import sys
# n은 회의의 수
n = int(sys.stdin.readline())
meetings = []
for _ in range(n):
    s, e = map(int, sys.stdin.readline().split())
    meetings.append([s,e])
select = []

s_m = sorted(meetings, key=lambda id:id[1])

for i in range(n):
    if not select:
        select.append(s_m[i])
        continue
    end = select[-1][1]
    if s_m[i][0] >= end:
        select.append(s_m[i])

print(len(select))