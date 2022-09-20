import sys
# n은 회의의 수
n = int(sys.stdin.readline())

# 시간이 가장 적게 소요되는 회의 중 끝나는 시간이 제일 큰 값을 고른다.
# 고른 회의와 겹치는 회의를 삭제한다. (시작 혹은 끝나는 시간이 회의 중간에 있는 것)
# 고를 수 있는 회의가 없을 때까지 반복한다.

meetings = []
for _ in range(n):
    s, e = map(int, sys.stdin.readline().split())
    meetings.append((s,e,e-s))
cnt = 0
sort_meeting = sorted(meetings, key=lambda meeting:(-meeting[2], meeting[1]))
while len(sort_meeting)>0:
# 튜플에 대해서 마지막 인자를 내림차순으로 정렬하고,
# 그리고 그 안에서 다음 두번째 인자를 기준으로 오름차순으로 정렬한다.
    # 제일 오른쪽에 있는 요소를 선택한다.
    select_meet = sort_meeting.pop()
    print(select_meet)
    cnt += 1
    start, end = select_meet[0], select_meet[1]
    for meeting in sort_meeting:
        if start<meeting[0]<end or start<meeting[1]<end:
            sort_meeting.remove(meeting)
        if meeting[0]<=start and meeting[1]>=end:
            sort_meeting.remove(meeting)

print(cnt)