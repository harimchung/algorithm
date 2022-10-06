import sys
def binary_search(s,e,target):
    middle = (s+e) // 2
    if s > e:
        print(0)
        return

    if target == nl[middle]:
        print(1)
        return
    elif target < nl[middle]:
        binary_search(s, middle-1, target)
    elif target > nl[middle]:
        binary_search(middle+1, e, target)

n = int(sys.stdin.readline())
nl = list(map(int, sys.stdin.readline().split()))
nl.sort()
m = int(sys.stdin.readline())
ml = list(map(int, sys.stdin.readline().split()))

i, j = 0, len(nl) - 1
for number in ml:
    binary_search(i, j, number)

