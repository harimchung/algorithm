import sys
sys.setrecursionlimit(10000)

def search(start, end, target, target_idx): # 이진탐색을 거친다.
    global ans  # start, end는 각각 시작과 끝 인덱스

    if start > end:
        return

    mid = (end+start)//2
    if nl[mid] == target: # 이진탐색의 결과가 목표한 숫자라면,



    elif nl[mid] < target: # 현재숫자 < 목표숫자이면, 시작지점을 키운다
        search(mid+1, end, target, target_idx)
    elif nl[mid] > target :
        search(start, mid, target, target_idx)



N = int(input())
nl = sorted(list(map(int, input().split())))
M = int(input())
ml = list(map(int, input().split()))
ans = [0] * M

for i in range(M):
    search(0, N, ml[i], i)
print(*ans)
