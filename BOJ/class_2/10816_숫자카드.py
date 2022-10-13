import sys

def lower_bound(array, target):
    left = 0
    right = len(array)

    while left < right:
        mid = (left+right) // 2
        if target <= array[mid]:
            right = mid
        else:
            left = mid+ 1
    return left

def upper_bound(array, target):
    left = 0
    right = len(array)
    while left < right:
        mid = (left+right) // 2
        if target >= array[mid]:
            left = mid + 1
        else:
            right = mid
    return left

N = int(sys.stdin.readline().rstrip())
nl = sorted(list(map(int, sys.stdin.readline().split())))
M = int(sys.stdin.readline().rstrip())
ml = list(map(int, sys.stdin.readline().split()))
ans = [0] * M

for i in range(M): # ml의 i 번째 인덱스를 찾아나섭니다.
    lb = lower_bound(nl, ml[i])
    ub = upper_bound(nl, ml[i])
    ans[i] = ub - lb

print(*ans)
