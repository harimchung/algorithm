import sys
# n은 회의의 수
n = int(sys.stdin.readline())
meetings = []
for _ in range(n):
    s, e = map(int, sys.stdin.readline().split())
    meetings.append([s,e])
select = []

s_m = sorted(meetings, key=lambda id:(id[1], id[0]))

for i in range(n):
    if not select:
        select.append(s_m[i])
        continue
    end = select[-1][1]
    if s_m[i][0] >= end:
        select.append(s_m[i])

print(len(select))