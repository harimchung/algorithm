import sys

n = int(sys.stdin.readline())
check = [0]*(2147483649)
check_minus = [0]*(2147483649)
a = list(map(int, sys.stdin.readline().split()))

for i in range(n):
    if a[i] < 0:
        check_minus[abs(a[i])] = 1
    else:
        check[a[i]] = 1

m = int(sys.stdin.readline())
b = list(map(int, sys.stdin.readline().split()))

for j in range(m):
    if b[j] < 0:
        print(check_minus[abs(b[j])])
    else:
        print(check[b[j]])

